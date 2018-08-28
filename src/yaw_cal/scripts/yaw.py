#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import String
from rosgraph_msgs.msg import Log
import atexit
import serial
import sys
import time

status=False

def rosout_callback(data):
    global status
    if (str(data.name) == "/rosbridge_websocket"):
        if (str(data.msg).split('.')[0] == "Client connected"):
            time.sleep(2)
            if status==True:
                alert.publish("YAW_TRUE")
            else:
                alert.publish("YAW_FALSE")



pub = rospy.Publisher('/yaw', Int16, queue_size=1)
rospy.Subscriber("/rosout", Log, rosout_callback)
alert = rospy.Publisher('alert', String, queue_size=50)
rospy.init_node('yaw_cal')
port = '/dev/serial/by-id/usb-Arduino__www.arduino.cc__Arduino_Mega_2560_952323438333515090C1-if00'
serial_port = serial.Serial(port, 115200)
once=False

#platform-12120000.usb-usb-0:1:1.0
#platform-xhci-hcd.3.auto-usb-0:1.1.4:1.0




while True :
    try:
    # serial_port.
        reading = serial_port.readline()
        pub.publish(int(reading))
        if status==False:
            alert.publish("YAW_TRUE")
            status=True
    except Exception as e:
        rospy.loginfo(e)
        if status==True:
            alert.publish("YAW_FALSE")
            status=False
        serial_port.reset_input_buffer()
        if status==True:
            status=False
        serial_port.close()

sys.exit(0)



# #!/usr/bin/env python
# import rospy
# from std_msgs.msg import Int16
# import threading
# import serial
# import atexit
# import sys

# connected = False
# port = '/dev/serial/by-path/platform-xhci-hcd.3.auto-usb-0:1.2:1.0-port0'
# baud = 115200
# stop = ""
# serial_port = serial.Serial(port, baud)


# class threadrun (threading.Thread):
#     def __init__(self, threadID):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#     def run(self):
#         global stop,serial_port
#         stopped = False
#         while True :
#             if stopped == False:
#                 try :
#                     reading = serial_port.readline()
#                     pub.publish(int(reading))
#                     if stop == "bye":
#                         serial_port.close()
#                         return True
#                 except serial.SerialException as e:
#                     serial_port.close()
#                     stopped = True
#                     rospy.loginfo("excepts" + str(e))
#             else :
#                 serial_port = serial.Serial(port, baud)
#                 stopped = False
#                 rospy.loginfo("excepts")

# def myhook():
#   global stop
#   stop = "bye"
#   serial_port.close()

# try :
#   pub = rospy.Publisher('/yaw', Int16, queue_size=1, latch = False)
#   rospy.init_node('yaw_cal')
#   thread = threadrun(1)
#   thread.start()
#   rospy.on_shutdown(myhook)   
#   # rospy.spin()
#   while True:
#       if stop == "bye":
#           print("main")
#           break
# except (KeyboardInterrupt, rospy.ROSInterruptException, serial.SerialException ) as e:
#   pass
    


    

