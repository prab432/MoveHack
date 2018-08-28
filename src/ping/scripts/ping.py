#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import time 
import datetime

pub = rospy.Publisher('/ping', String, queue_size=10)
rospy.init_node('ping')
r = rospy.Rate(1) # 1hz
while not rospy.is_shutdown():
   pub.publish(str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
   r.sleep()
