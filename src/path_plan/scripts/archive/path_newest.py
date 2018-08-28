#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import UInt16
from std_msgs.msg import Int16
from rosgraph_msgs.msg import Log
from path_plan.srv import angle
from path_plan.srv import marker
import time 
import threading
from path_plan.msg import AprilTagDetection,AprilTagDetectionArray
import geometry_msgs
import tf
import socket


final_dest = False

currentLoc = 0
goalLoc = 0
reached = False
stop = ""
sett = False
direc = 0
drive_auto = False
errangle = 0
yaw = 0
previous = True
execu = True
up=1


def move_funct_front_debug(current_id,next_id,direc,dist):
	move_until_marker_debug(next_id)
	time.sleep(1)
	return True 


def move_until_marker_debug(next_id): # needs to change
	pub.publish(str("moving:" + str(next_id)))


#######################################################################################
def callback_yaw(data):
	global yaw
	yaw=data.data

#######################################################################################

def callback_set(data):
	if data.data!="set":
		global currentLoc
		front_marker=req_front()
		currentLoc= int(front_marker.split(',')[1])
		pub.publish(str("at:"+currentLoc))

def move_until_dist(dist):
	drive_pub.publish("up")
	wait=False
	while wait == False:
		front_marker = req_front()
		if int(front_marker.split(',')[1]) == int(next_id) and float(front_marker.split(',')[4]) >= float(dist):
			wait = True 	
	drive_pub.publish("rup") 	


def move_until_marker(next_id): # needs to change
	drive_pub.publish("up")
	wait=False
	while wait == False:
		if int(req_front().split(',')[1]) == int(next_id):
			wait = True 	
	drive_pub.publish("rup") 	


def move_funct_front(current_id,next_id):
	if int(current_id) == 99 :
		# check_angle()	
		rospy.loginfo("moving:" + str(next_id))
		move_until_marker(next_id)
		direction(direc)
		pub.publish(str(next_id))	
	elif int(req_front().split(',')[1]) == int(current_id):#id detected
		# check_angle()
		rospy.loginfo("moving:" + str(next_id))
		move_until_marker(next_id)
		direction(direc)
		pub.publish(str(next_id))	
	return True 

#######################################################################################

def check_angle():#needs to change
	rot = rospy.ServiceProxy('anglediff',angle)
	wait=False
	while wait == False:
		if req_front() != "stop,999":
			wait = True
	error = int(float(req_front().split(',')[5])) - 180
	if error > 0:
		rospy.loginfo("right : " + str(error)) 
		drive_change_angle.publish(error)
		time.sleep(2)
	elif error < 0:
		rospy.loginfo("left : " + str(error))	
		drive_change_angle.publish(error)
		time.sleep(2)
	elif error == 0:
		 rospy.loginfo("no error")	
	

def direction(direc):
	rot = rospy.ServiceProxy('anglediff',angle)
	if str(direc) == str("right"):
		rot(90,1)
	elif str(direc) == str("left"):
		rot(90,0)
	elif str(direc) == str("comp"):
		rot(180,0)
	elif str(direc) == str("none"):
		pass
	return True
#####################################################################################
def check_dock_angle():
	global yaw
	rot = rospy.ServiceProxy('anglediff',angle)
	yawdiff=yaw-164
	if abs(yawdiff) >4:
		if yawdiff<0:
			rot((yawdiff-4),1)
		elif yawdiff>0:
			rot((yawdiff-4),0)

#######################################################################################
def zero():
	global up
	up=1
	######################################
	#check_dock_angle()
	#######################################
	return True

def nzero():
	global up
	#time.sleep(2)
	#direction("comp")
	if up==1:
		direction("comp")
		up=0
	move_funct_front(99,5)
	direction("comp")
	up=1
	#check_dock_angle()

	return True
	
#######################################################################################
def one():
	global up
	pub.publish("moving")
	if up==0:
		direction("comp")
		up=1	
	move_funct_front(0,1) # 6 -7
	#direction("left")
	return True
	
def none():
	global up
	if up==1:
		direction("comp")
		up=0
	move_funct_front(2,1)
	#direction("right")
	return True
	
#######################################################################################
def two():
	#top correction
	global up
	if up==0:
		direction("comp")
		up=1
	move_funct_front(1,2) # 7 -8
	#direction("comp")
	return True
	
def ntwo():
	global up
	if up==1:
		direction("comp")
		up=0
	#direction("comp")
	move_funct_front(3,2)
	return True
	
#######################################################################################
def three():
	global up
	if up==0:
		direction("comp")
		up=1
	move_funct_front(2,3) # 8 - 9
	return True

def nthree():
	global up
	if up==1:
		direction("comp")
		up=0
	#direction("comp")
	return move_funct_front_debug(4,3,"none",12)
	
#######################################################################################
def four():
	return move_funct_front(9,10) # 9 - 10
	
def nfour():
	return move_funct_front_debug(5,4,"none",12)
	
#######################################################################################
def five():
	return move_funct_front_debug(4,5,"none",12)
	
def nfive():
	return True
	
#######################################################################################
def six():
	return move_funct_front_debug(5,6,"comp",12)
	
def nsix():
	return move_funct_front_debug(6,5,"comp",12)
	
#######################################################################################
def seven():
	return move_funct_front_debug(6,7,"none",12)

def nseven():
	return move_funct_front_debug(7,6,"none",12)

#######################################################################################
def eight():
	return move_funct_front_debug(7,8,"none",12)

def neight():
	return move_funct_front_debug(8,7,"none",12)

#######################################################################################
def nine():
	return move_funct_front_debug(8,9,"none",12)

def nnine():
	return move_funct_front_debug(9,8,"none",12)

#######################################################################################
def ten():
	return move_funct_front_debug(9,10,"none",12)

def nten():
	return move_funct_front_debug(10,9,"none",12)

#######################################################################################

	

goalArray = [[zero,nzero],[one,none],[two,ntwo],[three,nthree],[four,nfour],[five,nfive],[six,nsix],[seven,nseven],[eight,neight],[nine,nnine],[ten,nten]]

def callback_goal(data):
	global currentLoc
	rospy.loginfo("got it")
	if sett == True :
		pass
	else:
		tt = int(data.data)
		if tt >= 0 :
			move(tt)
		else :
			pub.publish("currentLoc : " + str(currentLoc))


def move(position):
	global currentLoc,goalArray,reached,sett,previous
	sett = True
	reached = False
	while not reached:
		if int(position) < int(currentLoc) and previous == True:
			currentLoc -= 1
			rospy.loginfo(goalArray[currentLoc][1].__name__)
			temp = goalArray[currentLoc][1]()
			if temp == False :
				position = currentLoc
				previous = False
				pub.publish("error")
			else :
				pass
			time.sleep(1)
		elif int(position) > int(currentLoc) and previous == True:
			currentLoc += 1
			rospy.loginfo(goalArray[currentLoc][0].__name__)
			temp =  goalArray[currentLoc][0]()
			if temp == False :
				position = int(currentLoc)
				previous = False
				pub.publish("error")
			else :
				pass
			time.sleep(1)
		elif int(position) == int(currentLoc) and previous == True:
			pub.publish("reached:"+str(currentLoc))
			reached = True
			time.sleep(1)
		elif previous == False:
			pub.publish("error")
	sett = False




def rosout_callback(data):
    global currentLoc
    if (str(data.name) == "/rosbridge_websocket"):
        if (str(data.msg).split('.')[0] == "Client connected"):
            time.sleep(2)
            if int(req_front().split(',')[1]) == 999:
            	pub.publish("at:error")
            else	:
            	pub.publish("at:"+str(req_front().split(',')[1]))
            	currentLoc = int(req_front().split(',')[1])

       
def req_top():
    try:
        marker_top = rospy.ServiceProxy('marker_top', marker)
        resp = marker_top(0)
        temp = resp.output
        temp1 = temp.replace("6","0")
        return temp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def req_front():
    try:
        marker_front = rospy.ServiceProxy('marker_front', marker)
        resp = marker_front(0)
        temp = resp.output
        temp1 = temp.replace("6","0")
        return temp
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


def callback_current(data):
	global currentLoc
	currentLoc = int(data.data)
	pub.publish("at:"+str(int(data.data)))
	print "currentLoc change :"+ str(currentLoc)

def callback_correct(data):
	rot = rospy.ServiceProxy('anglediff',angle)
	rosout(int(data.data))


#time.sleep(1)
pub = rospy.Publisher('/pathstatus', String, queue_size=1)
drive_pub = rospy.Publisher('/simple_ctrl', String, queue_size=1)
rospy.init_node('path_plan')
#rospy.wait_for_service('marker_top')
rospy.wait_for_service('marker_front')
rospy.wait_for_service('anglediff')
rospy.Subscriber("/correct", String, callback_correct)
rospy.Subscriber("/goal_set", String, callback_goal)
rospy.Subscriber("/set_current", String, callback_current) 
rospy.Subscriber("/rosout", Log, rosout_callback)
rospy.Subscriber("/yaw", Int16, callback_yaw)
if execu == True :
	if int(req_front().split(',')[1]) == 999:
		pub.publish("at:error")
		rospy.loginfo("at : error")
	else:
		pub.publish("at:"+str(req_front().split(',')[1]))
		currentLoc = int(req_front().split(',')[1])
		rospy.loginfo("at : " + str(req_front().split(',')[1]))
	execu = False
rospy.spin()



