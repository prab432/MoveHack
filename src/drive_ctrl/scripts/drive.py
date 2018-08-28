#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from drive_ctrl.srv import angle
import threading
import RPi.GPIO as GPIO
import time
import atexit

stop = ""

left_cmd = 4
left_inc = 800
left_top = 800
left_bottom = 200
left_finite = False
left_acc = 0.003

right_cmd = 4
right_inc = 800
right_top = 800
right_bottom = 200
right_finite = False
right_acc = 0.003

gtg = True

sright = 0
sleft = 0
hright = 0
hleft = 0
up = 0
down = 0
right = 0
left = 0
lleft=0
lright=0
obstacle = False


#Pins definitions
MOTOR_LEFT_STEPS = 11
MOTOR_LEFT_DIR = 7
MOTOR_RIGHT_STEPS = 37
MOTOR_RIGHT_DIR = 35

#GPIO setup and init.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTOR_LEFT_STEPS, GPIO.OUT)
GPIO.setup(MOTOR_LEFT_DIR, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_STEPS, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_DIR, GPIO.OUT)

class left_thread (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global left_cmd,left_inc,left_top,left_bottom,left_finite,left_acc,stop
        while True and stop != "bye":
            if left_cmd == 2 : # rising delay
                while left_inc < left_top:
                    if left_cmd == 2 : 
                        left_inc +=  3# print left_inc
                        time.sleep(left_acc)
                    else :
                        break 
                left_finite = False #stop drive
                if left_cmd == 2:
                    left_cmd = 3
            if left_cmd == 1 : #falling delay
                left_finite = True #start drive
                while left_inc > left_bottom:
                    if left_cmd == 1: 
                        left_inc -=  3# print left_inc
                        time.sleep(left_acc)
                    else :
                        break
                if left_cmd == 1:
                    left_cmd = 3
            if left_cmd == 3 and left_inc == left_bottom:
                time.sleep(left_acc)
            
            if left_cmd == 3 and left_inc > left_bottom : 
                while left_inc > left_bottom:
                    if left_cmd != 2: 
                        left_inc -=  3# print left_inc
                        time.sleep(left_acc)
                    else :
                        break
            if left_cmd == 3 and left_inc < left_bottom:
                while left_inc < left_bottom:
                    if left_cmd != 2: 
                        left_inc +=  3# print left_inc
                        time.sleep(left_acc)
                    else :
                        break

            



class right_thread (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global right_cmd,right_inc,right_top,right_bottom,right_finite,right_acc,stop
        while True and stop != "bye":
            if right_cmd == 2 : # rising delay
                while right_inc < right_top:
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
                while right_inc > right_bottom:
                    if right_cmd == 1: 
                        right_inc -=  3# print right_inc
                        time.sleep(right_acc)
                    else :
                        break 
                if right_cmd == 1:
                    right_cmd = 3    
            if right_cmd == 3 and right_inc == right_bottom:
                time.sleep(left_acc)
            if right_cmd == 3 and right_inc > right_bottom : 
                while right_inc > right_bottom:
                    if right_cmd != 2: 
                        right_inc -=  3# print left_inc
                        time.sleep(right_acc)
                    else :
                        break
            if right_cmd == 3 and right_inc < right_bottom:
                while right_inc < right_bottom:
                    if right_cmd != 2: 
                        right_inc +=  3# print left_inc
                        time.sleep(right_acc)
                    else :
                        break
            
        


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

     

def drive_motor(delay_left,delay_right,left_dire,right_direc):
    global left_bottom,right_bottom,left_cmd,right_cmd,MOTOR_LEFT_DIR,MOTOR_RIGHT_DIR
    left_bottom = delay_left
    right_bottom = delay_right
    left_cmd = 1
    right_cmd = 1
    GPIO.output(MOTOR_LEFT_DIR,left_dire)
    GPIO.output(MOTOR_RIGHT_DIR,right_direc)

    

def stop_motor():
    global left_cmd,right_cmd
    left_cmd = 2
    right_cmd = 2  



def callback(data):
    global up,down,left,right,left_bottom,right_bottom,obstacle,sleft,sright,hright,hleft,gtg,lleft,lright
    rot = rospy.ServiceProxy('anglediff',angle)
    if gtg == True :    
        if str(data.data) == "up" and up == 0 and obstacle != True:
            drive_motor(900,900,1,0) #500
            up = 1
        elif str(data.data) == "down" and down == 0 :
            drive_motor(600,600,0,1)
            down = 1
        elif str(data.data) == "right" and right == 0 :
            drive_motor(900,900,1,1)
            right = 1
        elif str(data.data) == "left" and left == 0 :
            drive_motor(900,900,0,0)
            left = 1
        elif str(data.data) == "rup" and up == 1:
            stop_motor()
            up = 0
        elif str(data.data) == "rdown" and down == 1:
            stop_motor()
            down = 0
        elif str(data.data) == "rleft" and left == 1:
            stop_motor()
            left = 0
        elif str(data.data) == "rright" and right == 1:
            stop_motor()
            right = 0
        elif str(data.data) == "stop":
            stop_motor()
        elif str(data.data) == "sleft" and sleft == 0:
            left_bottom = 1000
            right_bottom = 800
            sleft = 1
        elif str(data.data) == "rsleft" and lleft == 1:
            left_bottom = 900
            right_bottom= 900
            lleft = 0
	    sleft=0
        elif str(data.data) == "sright" and sright == 0:
            right_bottom= 1000
            left_bottom = 800
            sright = 1
        elif str(data.data) == "rsright" and lright == 1:
            right_bottom = 900 #900
            left_bottom = 900 #500
            lright = 0
	    sright=0
        elif str(data.data) == "lright" and lright == 0:
            right_bottom = 1500 #1500
            left_bottom = 500 #400
            lright=1
        elif str(data.data) == "lleft" and lleft == 0:
            right_bottom = 500 #400
            left_bottom = 1500 #1500
            lleft=1


        elif str(data.data)=="hright":
            rot(90,1)
        elif str(data.data)=="hleft" :
            rot(90,0)
    

def service_callback(data):
    if int(str(data.data).split(",")[0]) == 0 and int(str(data.data).split(",")[1]) == 0 : 
        stop() 
    else :
        drive_motor(int(str(data.data).split(",")[0]),int(str(data.data).split(",")[1]),1,0)
                 

def myhook():
    global stop
    stop = "bye"
    GPIO.cleanup()


def obstacle_callback(data):
    global up,obstacle,left_cmd,right_cmd
    cmd = str(data.data)
    cmd_digits = [int(d) for d in str(cmd)]
    if cmd == "00000000":
        obstacle = False
        if up ==  1 :
            rospy.loginfo("up")
            left_cmd = 1
            right_cmd = 1 
    elif cmd_digits[4:] > [0,0,0,0] or cmd_digits[0] == 1 or cmd_digits[2] == 1:
        obstacle = True
        if up == 1:  
            rospy.loginfo("rup")
            stop_motor()
  
def alert_callback(data):
    global gtg
    if str(data.data) == "yaw-start":
        gtg = True
    elif str(data.data) == "yaw-stop":
        gtg = False
        stop_motor()

try :
    # Create new threads
    thread1 = left_thread(1)
    thread2 = right_thread(1)
    thread3 = left_steps(1)
    thread4 = right_steps(1)

    # Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    
    rospy.init_node('drive_ctrl')
    rospy.wait_for_service('anglediff')
    rospy.Subscriber("/simple_ctrl", String, callback)
    rospy.Subscriber("/final_send", String, obstacle_callback)
    rospy.Subscriber("/service_callback", String, service_callback)
    rospy.Subscriber("/alert", String, alert_callback)
    rospy.on_shutdown(myhook)
    rospy.spin()

except (KeyboardInterrupt,rospy.ROSException):
    stop = "bye"
    GPIO.cleanup()



@atexit.register
def cleanup():
    stop = "bye"
    GPIO.cleanup()
