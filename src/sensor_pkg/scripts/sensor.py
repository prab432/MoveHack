#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16
import time
import threading
import atexit

sensor_one_thres = rospy.get_param('/sensor_one_thres', '1000') # top
sensor_two_thres = rospy.get_param('/sensor_two_thres', '600') # left 
sensor_three_thres = rospy.get_param('/sensor_three_thres', '700') # center
sensor_four_thres = rospy.get_param('/sensor_four_thres', '600') # right

sensor_one = 0
sensor_two = 0
sensor_three = 0
sensor_four = 0

stop = ""

class allclear(threading.Thread):
    """docstring for allclear"""
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global sensor_one_thres,sensor_two_thres,sensor_three_thres,sensor_four_thres,sensor_one,sensor_two,sensor_three,sensor_four,stop
        while True and stop != "bye":
        	time.sleep(1)
        	if int(sensor_one) > int(sensor_one_thres) and int(sensor_two) > int(sensor_two_thres) and int(sensor_three) > int(sensor_three_thres) and int(sensor_four) > int(sensor_four_thres):
        		pub.publish('path_clear')
        		
        	

def callback_one(data):
	global sensor_one_thres,sensor_one
	# rospy.loginfo("sensor one %s", data.data)
	sensor_one = str(data.data)
	if int(sensor_one) <= int(sensor_one_thres):
		pub.publish('obstacle_top')

def callback_two(data):
	global sensor_two_thres,sensor_two
	# rospy.loginfo("sensor two %s", data.data)
	sensor_two = str(data.data)
	if int(sensor_two) <= int(sensor_two_thres):
		pub.publish('obstacle_left')

def callback_three(data):
	global sensor_three_thres,sensor_three
	# rospy.loginfo("sensor three %s", data.data)
	sensor_three = str(data.data)
	if int(sensor_three) <= int(sensor_three_thres):
		pub.publish('obstacle_center')

def callback_four(data):
	global sensor_four_thres,sensor_four
	# rospy.loginfo("sensor four %s", data.data)
	sensor_four = str(data.data)
	if int(sensor_four) <= int(sensor_four_thres):
		pub.publish('obstacle_right')


def myhook():
    global stop
    stop = "bye"

if __name__ == '__main__':
	try:
		pub = rospy.Publisher('/obstacle', String, queue_size=5)
		rospy.init_node('sensor_pkg')
		rospy.Subscriber("/range_data_top", UInt16, callback_one)
		rospy.Subscriber("/range_data_left", UInt16, callback_two)
		rospy.Subscriber("/range_data_center", UInt16, callback_three)
		rospy.Subscriber("/range_data_right", UInt16, callback_four)
		thread = allclear(1)
		thread.start()
		rospy.on_shutdown(myhook)
		rospy.spin()
	except (KeyboardInterrupt,rospy.ROSException):
		stop = "bye"


@atexit.register
def cleanup():
    stop = "bye"



# demo codes


# def callback_one(data):
# 	global sensor_one_thres,sensor_one
# 	# rospy.loginfo("sensor one %s", data.data)
# 	sensor_one = str(data.data)
# 	if int(sensor_one) <= int(sensor_one_thres):
# 		pub.publish('obstacle_one')
# 	# else :
# 	#    global sensor_two_thres
# 	#    global sensor_three_thres
# 	#    global sensor_four_thres
# 	#    # rospy.loginfo("sensor two %s", data.data)
# 	#    sensor_two = str(data.data) 
# 	#    # rospy.loginfo("sensor three %s", data.data)
# 	#    sensor_three = str(data.data) 
# 	#    # rospy.loginfo("sensor four %s", data.data)
# 	#    sensor_four = str(data.data) 
# 	#    if   int(sensor_two) > int(sensor_two_thres) and int(sensor_three) > int(sensor_three_thres) and int(sensor_four) > int(sensor_four_thres):
# 	# 	pub.publish('path_clear')
