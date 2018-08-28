#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import threading
import RPi.GPIO as GPIO
import time
import atexit

stop = ""

left_cmd = 3
left_inc = 800
left_top = 800
left_bottom = 200
left_finite = False
left_acc = 0.003


up = 0
down = 0
right = 0
left = 0

#Pins definitions
MOTOR_LEFT_STEPS = 11
MOTOR_LEFT_DIR = 7

#GPIO setup and init.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTOR_LEFT_STEPS, GPIO.OUT)
GPIO.setup(MOTOR_LEFT_DIR, GPIO.OUT)

class left_thread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global left_cmd,left_inc,left_top,left_bottom,left_finite,left_acc,stop
        while True :
            prev = left_bottom
            if left_cmd == 2 : # rising delay
                while True and stop != "bye" and left_inc < left_top:
                    if left_cmd == 2 : 
                        left_inc +=  3# print left_inc
                        time.sleep(left_acc)
                    else :
                        break 
                left_finite = False #stop drive
                if left_cmd == 2:
                    left_cmd = 3
                    pass
            if left_cmd == 1 : #falling delay
                left_finite = True #start drive
                while True and stop != "bye" and left_inc > left_bottom:
                    if left_cmd == 1: 
                        left_inc -=  3# print left_inc
                        time.sleep(left_acc)
                    else :
                        break   
                if left_cmd == 1:
                    left_cmd = 3
            if left_cmd ==3 :
                time.sleep(left_acc)                
                if stop == "bye" :
                    print "exit from thread"
                    return False
            if stop == "bye" :
                print "exit from thread"
                return False

class left_steps(threading.Thread):
    """docstring for left_steps"""
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global left_finite,left_inc,stop,MOTOR_LEFT_STEPS
        while True:
            while left_finite:
                GPIO.output(MOTOR_LEFT_STEPS,1)
                time.sleep(abs((left_inc)/1000000.0))
                GPIO.output(MOTOR_LEFT_STEPS,0)
                time.sleep(abs((left_inc)/1000000.0)) 
                if stop == "bye" :
                    print "exit from thread"
                    return False    
            if stop == "bye" :
                    print "exit from thread"
                    return False
                                

     

def drive_motor(delay,left_dire):
    global left_bottom,left_cmd,MOTOR_LEFT_DIR
    left_bottom = delay
    left_cmd = 1
    GPIO.output(MOTOR_LEFT_DIR,left_dire)


def stop_motor():
    global left_cmd
    left_cmd = 2


def callback(data):
    global up,down,left,right,sleft,sright
    if str(data.data) == "up" and up == 0 :
        rospy.loginfo("up")
        drive_motor(500,1)
        up = 1
    elif str(data.data) == "down" and down == 0:
        rospy.loginfo("down")
        drive_motor(500,0)
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
            drive_motor(500,1)
    elif cmd == "obstacle_top" or cmd == "obstacle_center":
        if up == 1:  
            rospy.loginfo("rup")
            stop_motor()
       

try :
    # Create new threads
    thread1 = left_thread(1)
    thread3 = left_steps(1)

    # Start new Threads
    thread1.start()
    thread3.start()
    
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

