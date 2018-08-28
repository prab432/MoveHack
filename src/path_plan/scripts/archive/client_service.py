#! /usr/bin/env python

import socket
import time
import sys
import rospy
from path_plan.srv import *

def marker_front_client():
    try:
        marker_front = rospy.ServiceProxy('marker_front', marker)
        resp = marker_front(0)
        return resp.output
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def marker_top_client():
    try:
        marker_top = rospy.ServiceProxy('marker_top', marker)
        resp = marker_top(0)
        return resp.output
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    rospy.wait_for_service('marker_front')
    rospy.wait_for_service('marker_top')
    for i in range(0,100):
        print str(marker_front_client())
        print str(marker_top_client())


rospy.wait_for_service('marker_top')
marker_top = rospy.ServiceProxy('marker_top', marker)
resp = marker_top(0)
print resp.output