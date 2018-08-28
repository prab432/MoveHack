#!/usr/bin/env python
import rospy
from std_msgs.msg import String
#from std_msgs.msg import Int16
from std_msgs.msg import Int16
import threading
import RPi.GPIO as GPIO
import time
import atexit
line_dev = 0 
enable_correction = False
error=0
stop=""
kp=10

def calldev(data):
    global error
    error = int(data.data)
    #yaw=255-yaw
    #rospy.loginfo(yaw)
    
def myhook():
    global stop
    stop="bye"
    exit(0)



def callback(data):
    global enable_correction
    if str(data.data) == "up" :
        enable_correction = True
    elif str(data.data) == "rup": 
        enable_correction = False



class correction_thread(threading.Thread):
    """docstring for correction_thread"""
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global enable_correction,error,line_dev,stop
        sleft = 0 
        sright = 0 

        while True and stop != "bye":
            #error=getLineError(line_dev)
            #error_pub.publish(error)
            while enable_correction==True:
                #if yaw > direc:
                speed= kp* error
                drive_pub.publish("line," + str(speed))

                      




try:
    drive_pub = rospy.Publisher('/simple_ctrl', String, queue_size=1)
    rospy.init_node('correction')

    rospy.Subscriber("/error", Int16, calldev)
    #rospy.Subscriber("/line_raw", Int16, calldev)
    rospy.Subscriber("/simple_ctrl", String, callback)
    thread = correction_thread(1)
    thread.start()
    rospy.on_shutdown(myhook)
    rospy.spin()
except (KeyboardInterrupt,rospy.ROSException) as e:
    print(e)



