#!/usr/bin/env python
import rospy
from std_msgs.msg import String
#from std_msgs.msg import Int16
from std_msgs.msg import Int16
import threading
import RPi.GPIO as GPIO
import time
import atexit
from rosgraph_msgs.msg import Log

line_dev = 0 
enable_correction = False
error=0
stop=""
path=False


def rosout_callback(data):
    global path
    if (str(data.name) == "/rosbridge_websocket"):
        if (str(data.msg).split('.')[0] == "Client connected"):
            time.sleep(2)
            if path==True:
                alert.publish("PATH_TRUE")
            else:
                alert.publish("PATH_FALSE")


def getLineError(line):
    # print "{0:b}".format(line)
    accumulator=0
    count=0
    #counting 
    for shift in range(0, 8):
        if (line>>shift & 0x01):
            # print "Count " + str(shift)
            count=count+1
    #LSB
    for shift in range(0,4):
        if (line>>shift & 0x01):
            # print "LSB " + str(shift) + " # " + str((32 * (4 - shift)) - 1)
            accumulator += ((32 * (4 - shift)) - 1)
    #MSB
    for shift in range(4,8):
        if (line>>shift & 0x01):
            # print "MSB " + str(shift) + " # " + str((-32 * (shift - 3)) + 1)
            accumulator += ((-32 * (shift - 3)) + 1)
    # print "Accumulator" + str(accumulator)
    # print "Count      " + str(count)
    # print "Error      " + str(accumulator/count)
    if count !=0:
        return accumulator/count
    else :
        return 0


def calldev(data):
    global line_dev,error
    line_dev = int(data.data)
    error=getLineError(line_dev)
    #error_pub.publish(error)
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
        global enable_correction,error,line_dev,stop,path
        sleft = 0 
        sright = 0 
        if path==False:
        	alert.publish("PATH_TRUE")
        	path=True
        while True and stop != "bye":
            #error=getLineError(line_dev)
            #error_pub.publish(error)
            while enable_correction==True:
                #if yaw > direc:

                      
                # if line_dev<24 :
                #         if sleft == 0 :
                #             rospy.loginfo("lleft")
                #             drive_pub.publish("lleft")
                #             sleft = 1
                # elif line_dev>24 :
                #         if sright == 0 :
                #             rospy.loginfo("lright")
                #             drive_pub.publish("lright")
                #             sright = 1
                # else :
                #         if sright == 1 :
                #             drive_pub.publish("rsright")
                #             sright = 0
                #         if sleft == 1 :
                #             drive_pub.publish("rsleft")
                #             sleft = 0

                # drive_pub.publish("line ," + str(error))
                if error>0:
                        if sleft == 0 :
                            rospy.loginfo("lleft")
                            drive_pub.publish("lleft")
                            sleft = 1
                elif error<0:
                        if sright == 0 :
                            rospy.loginfo("lright")
                            drive_pub.publish("lright")
                            sright = 1
                else :
                        if line_dev==0:
                            drive_pub.publish("rup")
                            if path==True:
                            	alert.publish("PATH_FALSE")
                            	path=False
                        if sright == 1 :
                            drive_pub.publish("rsright")
                            sright = 0
                        if sleft == 1 :
                            drive_pub.publish("rsleft")
                            sleft = 0






try:
    drive_pub = rospy.Publisher('/simple_ctrl', String, queue_size=1)
    rospy.init_node('correction')
    alert = rospy.Publisher('alert', String, queue_size=50)

    #rospy.Subscriber("/yaw2", Int16, callyaw)
    rospy.Subscriber("/line_raw", Int16, calldev)
    rospy.Subscriber("/simple_ctrl", String, callback)
    rospy.Subscriber("/rosout", Log, rosout_callback)
    error_pub = rospy.Publisher("/error",Int16,queue_size=1)
    thread = correction_thread(1)
    thread.start()
    rospy.on_shutdown(myhook)
    rospy.spin()
except (KeyboardInterrupt,rospy.ROSException) as e:
    print(e)