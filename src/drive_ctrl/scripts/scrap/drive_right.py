#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import threading
import RPi.GPIO as GPIO
import time
import atexit

stop = ""

right_cmd = 3
right_inc = 800
right_top = 800
right_bottom = 200
right_finite = False
right_acc = 0.003


up = 0
down = 0
right = 0
left = 0

#Pins definitions
MOTOR_RIGHT_STEPS = 37
MOTOR_RIGHT_DIR = 35

#GPIO setup and init.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTOR_RIGHT_STEPS, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_DIR, GPIO.OUT)

class right_thread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global right_cmd,right_inc,right_top,right_bottom,right_finite,right_acc,stop
        while True :
            prev = right_bottom
            if right_cmd == 2 : # rising delay
                while True and stop != "bye" and right_inc < right_top:
                    if right_cmd == 2 : 
                        right_inc += 3  #print right_inc
                        time.sleep(right_acc)
                    else :
                        break 
                right_finite = False # stop drive           
                if right_cmd == 2:
                    right_cmd = 3
            if right_cmd == 1 : #falling delay
                right_finite = True # start drive
                while True and stop != "bye" and right_inc > right_bottom:
                    if right_cmd == 1: 
                        right_inc -=  3# print right_inc
                        time.sleep(right_acc)
                    else :
                        break   
                if right_cmd == 1:
                    right_cmd = 3    
            if right_cmd == 3 :
                time.sleep(right_acc)               
                if stop == "bye" :
                    print "exit from thread"
                    return False
                    
            if stop == "bye" :
                print "exit from thread"
                return False      
        
class right_steps(threading.Thread):
    """docstring for left_steps"""
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global right_finite,right_inc,stop,MOTOR_RIGHT_STEPS
        while True:
            while right_finite:
                GPIO.output(MOTOR_RIGHT_STEPS,1)
                time.sleep(abs(right_inc/1000000.0))
                GPIO.output(MOTOR_RIGHT_STEPS,0)
                time.sleep(abs(right_inc/1000000.0))  
                if stop == "bye" :
                    print "exit from thread"
                    return False
            if stop == "bye" :
                    print "exit from thread"
                    return False

     

def drive_motor(delay,right_direc):
    global left_bottom,right_cmd,MOTOR_LEFT_DIR
    right_bottom = delay
    right_cmd = 1
    GPIO.output(MOTOR_RIGHT_DIR,right_direc)


def stop_motor():
    global right_cmd
    right_cmd = 2  



def callback(data):
    global up,down,left,right,sleft,sright
    if str(data.data) == "up" and up == 0 :
        rospy.loginfo("up")
        drive_motor(500,0)
        up = 1
    elif str(data.data) == "down" and down == 0:
        rospy.loginfo("down")
        drive_motor(500,1)
        down = 1
    elif str(data.data) == "right" and right == 0:
        rospy.loginfo("right")
        drive_motor(800,1)
        right = 1
    elif str(data.data) == "left" and left == 0:
        rospy.loginfo("left")
        drive_motor(800,0)
        left = 1

    elif str(data.data) == "rup" and up == 1:
        rospy.loginfo("rup")
        stop_motor()
        up = 0
    elif str(data.data) == "rdown" and down == 1:
        rospy.loginfo("rdown")
        stop_motor()
        down = 0
    elif str(data.data) == "rleft" and left == 1:
        rospy.loginfo("rleft")
        stop_motor()
        left = 0
    elif str(data.data) == "rright" and right == 1:
        rospy.loginfo("rright")
        stop_motor()
        right = 0
    elif str(data.data) == "stop":
        rospy.loginfo("release")    
        stop_motor()
    

def myhook():
    global stop
    stop = "bye"
    GPIO.cleanup()


def obstacle_callback(data):
    global up,down,left,right,aup,adown,aright,aleft
    cmd = str(data.data)
    if cmd == "path_clear":
        if up ==  1 :
            rospy.loginfo("up")
            drive_motor(500,0)
    elif cmd == "obstacle_top" or cmd == "obstacle_center":
        if up == 1:  
            rospy.loginfo("rup")
            stop_motor()
       

try :
    # Create new threads
    thread2 = right_thread(1)
    thread4 = right_steps(1)

    # Start new Threads
    thread2.start()
    thread4.start()
    
    rospy.init_node('drive_ctrl')
    rospy.Subscriber("/simple_ctrl", String, callback)
    rospy.Subscriber("/obstacle", String, obstacle_callback)
    rospy.on_shutdown(myhook)
    rospy.spin()

except (KeyboardInterrupt,rospy.ROSException):
    stop = "bye"
    GPIO.cleanup()



@atexit.register
def cleanup():
    stop = "bye"
    GPIO.cleanup()


