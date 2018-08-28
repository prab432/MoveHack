#! /usr/bin/env python
import rospy
from path_plan.msg import AprilTagDetection,AprilTagDetectionArray
import geometry_msgs
import tf
import sys
from std_msgs.msg import String
from rosgraph_msgs.msg import Log
from path_plan.srv import *

front_marker = "stop,999"
stop = ""
status=False
def rosout_callback(data):
    global status
    if (str(data.name) == "/rosbridge_websocket"):
        if (str(data.msg).split('.')[0] == "Client connected"):
            time.sleep(2)
            if status==True:
                alert.publish("CAMERA_TRUE")
            else:
                alert.publish("CAMERA_FALSE")


def handle_service_front(req):
    global front_marker
    return str(front_marker)

def myhook():
    global stop
    stop = "bye"

def callback_front(data):
    global front_marker,status
    detections = data.detections
    #status=True
    if status==False:
        alert.publish("CAMERA_TRUE")
        status=True
    if (len(detections)>0) :
        quaternion = (
        detections[0].pose.pose.orientation.x,
        detections[0].pose.pose.orientation.y,
        detections[0].pose.pose.orientation.z,
        detections[0].pose.pose.orientation.w)
        euler = tf.transformations.euler_from_quaternion(quaternion)
        yaw = 180+round((float(euler[2])*180)/3.14)
        front_marker = "front_detect,"+str(detections[0].id)+","+str(round((detections[0].pose.pose.position.x)*100))+","+str(round((detections[0].pose.pose.position.y)*100))+","+str(round((detections[0].pose.pose.position.z)*100))+","+str(yaw)
    else : 
        front_marker = "stop,999"
  
rospy.Subscriber("/aruco_front/tag_detections", AprilTagDetectionArray, callback_front)   
rospy.Subscriber("/rosout", Log, rosout_callback)
alert = rospy.Publisher('/alert', String, queue_size=50)
rospy.init_node('pathplan_front')
service_front = rospy.Service('marker_front', marker, handle_service_front)
rospy.on_shutdown(myhook)
rospy.spin()    

