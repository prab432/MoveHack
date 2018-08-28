#! /usr/bin/env python
import rospy
from path_plan.msg import AprilTagDetection,AprilTagDetectionArray
import geometry_msgs
import tf
import sys
from path_plan.srv import *

top_marker = "stop,999"
stop = ""

def handle_service_top(req):
    global front_marker
    return str(top_marker)

def myhook():
    global stop
    stop = "bye"

def callback_top(data):
    global top_marker
    detections = data.detections
    if (len(detections)>0) :
        quaternion = (
        detections[0].pose.pose.orientation.x,
        detections[0].pose.pose.orientation.y,
        detections[0].pose.pose.orientation.z,
        detections[0].pose.pose.orientation.w)
        euler = tf.transformations.euler_from_quaternion(quaternion)
        yaw = 180+round((float(euler[2])*180)/3.14)
        top_marker = "top_detect,"+str(detections[0].id)+","+str(round((detections[0].pose.pose.position.x)*100))+","+str(round((detections[0].pose.pose.position.y)*100))+","+str(round((detections[0].pose.pose.position.z)*100))+","+str(yaw)
    else : 
        top_marker ="stop,999"

rospy.Subscriber("/aruco_top/tag_detections", AprilTagDetectionArray, callback_top)   
rospy.init_node('pathplan_top')
service_top = rospy.Service('marker_top', marker, handle_service_top)
rospy.on_shutdown(myhook)
rospy.spin()    

