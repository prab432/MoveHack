#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
import time
import atexit
yaw = 0 
direc = 0
offset = 4 #angle juggad

def callyaw(data):
    global yaw
    yaw = int(data.data)
    

def myhook():
    global stop
    exit(0)


def callback(data):
    global yaw,direc,offset
    if str(data.data) == "hright" :
        pubbed = True
        direc = yaw
        final = direc+90
        if final >= 359:
            final =  abs(final) - 359
        rospy.loginfo(final)
        while yaw != final - offset:
            if pubbed == True:
                drive_pub.publish("right")
                pubbed = False
        drive_pub.publish("rright")
    elif str(data.data) == "hleft" :
        pubbed = True
        direc = yaw
        final = direc-90
        if final <= 0:
            final = 359 - abs(final)
        rospy.loginfo(final)    
        while yaw != final + offset:
            if pubbed == True:
                drive_pub.publish("left")
                pubbed = False 
        drive_pub.publish("rleft")
    # drive_pub.publish("stop")
    


def callangle(data):
    global yaw
    pubbed = True
    if int(data.data) > yaw :
        rospy.loginfo("right")
        while yaw != int(data.data) - offset:
            if pubbed == True:
                drive_pub.publish("right")
                pubbed = False
        drive_pub.publish("rright")

    elif int(data.data) < yaw :
        rospy.loginfo("left")
        while yaw != int(data.data) + offset:
            if pubbed == True:
                drive_pub.publish("left")        
                pubbed = False 
        drive_pub.publish("rleft")
    # drive_pub.publish("stop")


def callchangeangle(data):
    global yaw
    pubbed = True
    error = int(data.data)
    direc = yaw + error
    if direc > yaw:
        rospy.loginfo("right")
        while yaw != direc - offset:
            if pubbed == True:
                drive_pub.publish("right")        
                pubbed = False
        drive_pub.publish("rright")
    elif direc < yaw:
        while yaw != direc + offset:
            if pubbed == True:
                drive_pub.publish("left")        
                pubbed = False 
        drive_pub.publish("rleft")
    # drive_pub.publish("stop")
    

try:
    drive_pub = rospy.Publisher('/simple_ctrl', String, queue_size=1)
    rospy.init_node('yaw_correction')
    rospy.Subscriber("/yaw", Int16, callyaw)
    rospy.Subscriber("/angle", Int16, callangle)
    rospy.Subscriber("/change_angle", Int16, callchangeangle)
    rospy.Subscriber("/simple_ctrl", String, callback)
    rospy.on_shutdown(myhook)
    rospy.spin()
except (KeyboardInterrupt,rospy.ROSException) as e:
    print(e)
