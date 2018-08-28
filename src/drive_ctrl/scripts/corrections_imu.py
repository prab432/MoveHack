#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
import threading
import RPi.GPIO as GPIO
import time
import atexit
yaw = 0 
enable_correction = False
direc = 0
offset = 4 #angle juggad
stop = ""


def callyaw(data):
    global yaw
    yaw = int(data.data)
    
def myhook():
    global stop
    stop="bye"
    exit(0)

#def callset(data):
    #global direc,yaw
    #direc=yaw

def callback(data):
    global enable_correction,direc,yaw
    if str(data.data) == "up" :
        rospy.loginfo(yaw) 
        direc = yaw
        enable_correction = True
    elif str(data.data) == "rup":
        rospy.loginfo(yaw) 
        enable_correction = False



class correction_thread(threading.Thread):
    """docstring for correction_thread"""
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global yaw,enable_correction,stop,direc
        sleft = 0 
        sright = 0 
        while True and stop != "bye":
            while enable_correction:
                if yaw > direc:
                    if sleft == 0 :
                        drive_pub.publish("sleft")
                        sleft = 1
                elif yaw < direc:
                    if sright == 0 :
                        drive_pub.publish("sright")
                        sright = 1
                else :
                    if sright == 1 :
                        drive_pub.publish("rsright")
                        sright = 0
                    if sleft == 1 :
                        drive_pub.publish("rsleft")
                        sleft = 0
                    




try:
    drive_pub = rospy.Publisher('/simple_ctrl', String, queue_size=1)
    rospy.init_node('correction')
    rospy.Subscriber("/yaw", Int16, callyaw)
    rospy.Subscriber("/simple_ctrl", String, callback)
    #rospy.Subscriber("/set_imu",String,callset)
    thread = correction_thread(1)
    thread.start()
    rospy.on_shutdown(myhook)
    rospy.spin()
except (KeyboardInterrupt,rospy.ROSException) as e:
    print(e)


