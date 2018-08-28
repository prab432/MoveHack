# #!/usr/bin/env python
# import rospy
# from std_msgs.msg import String
# from std_msgs.msg import Float32
# import threading
# import RPi.GPIO as GPIO
# import time
# import atexit
# import serial

# stop = ""

# left_cmd = 3
# left_inc = 800
# left_top = 800
# left_bottom = 200
# left_finite = False
# left_acc = 0.003

# right_cmd = 3
# right_inc = 800
# right_top = 800
# right_bottom = 200
# right_finite = False
# right_acc = 0.003

# drive_auto = False
# start_drive = False
# direc = 0
# yaw = 0
# error_num = 0

# #Pins definitions
# MOTOR_LEFT_STEPS = 11
# MOTOR_LEFT_DIR = 7
# MOTOR_RIGHT_STEPS = 37
# MOTOR_RIGHT_DIR = 35



# #GPIO setup and init.
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(MOTOR_LEFT_STEPS, GPIO.OUT)
# GPIO.setup(MOTOR_LEFT_DIR, GPIO.OUT)
# GPIO.setup(MOTOR_RIGHT_STEPS, GPIO.OUT)
# GPIO.setup(MOTOR_RIGHT_DIR, GPIO.OUT)

# class left_thread (threading.Thread):
#     def __init__(self, threadID):
#         threading.Thread.__init__(self)
#         self.threadID = threadID

#     def run(self):
#         global left_cmd,left_inc,left_top,left_bottom,left_finite,left_acc,stop
#         while True :

#             if left_cmd == 2 : # rising delay
#                 while True and stop != "bye" and left_inc < left_top:
#                     if left_cmd == 2 : 
#                         left_inc +=  3# print left_inc
#                         time.sleep(left_acc)
#                     else :
#                         break 
#                 left_finite = False #stop drive

#             if left_cmd == 1 : #falling delay
#                 left_finite = True #start drive
#                 while True and stop != "bye" and left_inc > left_bottom:
#                     if left_cmd == 1: 
#                         left_inc -=  3# print left_inc
#                         time.sleep(left_acc)
#                     else :
#                         break   
#                 # while True and stop != "bye" and left_inc < left_bottom:
#                 #     if left_cmd == 1: 
#                 #         left_inc +=  3# print left_inc
#                 #         time.sleep(left_acc)
#                 #     else :
#                 #         break  
                

#             time.sleep(left_acc)                
#             if stop == "bye" :
#                 print "exit from thread"
#                 return False



# class right_thread (threading.Thread):
#     def __init__(self, threadID):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#     def run(self):
#         global right_cmd,right_inc,right_top,right_bottom,right_finite,right_acc,stop
#         while True :
            
#             if right_cmd == 2 : # rising delay
#                 while True and stop != "bye" and right_inc < right_top:
#                     if right_cmd == 2 : 
#                         right_inc += 3  #print right_inc
#                         time.sleep(right_acc)
#                     else :
#                         break 
#                 right_finite = False # stop drive           
                
#             if right_cmd == 1 : #falling delay
#                 right_finite = True # start drive
#                 while True and stop != "bye" and right_inc > right_bottom:
#                     if right_cmd == 1: 
#                         right_inc -=  3# print right_inc
#                         time.sleep(right_acc)
#                     else :
#                         break  
#                 # while True and stop != "bye" and right_inc < right_bottom:
#                 #     if right_cmd == 1: 
#                 #         right_inc +=  3# print right_inc
#                 #         time.sleep(right_acc)
#                 #     else :
#                 #         break   
            
#             time.sleep(right_acc)               
#             if stop == "bye" :
#                 print "exit from thread"
#                 return False


# class left_steps(threading.Thread):
#     """docstring for left_steps"""
#     def __init__(self, threadID):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#     def run(self):
#         global left_finite,left_inc,stop,MOTOR_LEFT_STEPS
#         while True:
#             while left_finite:
#                 GPIO.output(MOTOR_LEFT_STEPS,1)
#                 time.sleep(abs((left_inc)/1000000.0))
#                 GPIO.output(MOTOR_LEFT_STEPS,0)
#                 time.sleep(abs((left_inc)/1000000.0)) 
#                 if stop == "bye" :
#                     print "exit from thread"
#                     return False    
#             if stop == "bye" :
#                     print "exit from thread"
#                     return False
                                
        
# class right_steps(threading.Thread):
#     """docstring for left_steps"""
#     def __init__(self, threadID):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#     def run(self):
#         global right_finite,right_inc,stop,MOTOR_RIGHT_STEPS
#         while True:
#             while right_finite:
#                 GPIO.output(MOTOR_RIGHT_STEPS,1)
#                 time.sleep(abs(right_inc/1000000.0))
#                 GPIO.output(MOTOR_RIGHT_STEPS,0)
#                 time.sleep(abs(right_inc/1000000.0))  
#                 if stop == "bye" :
#                     print "exit from thread"
#                     return False
#             if stop == "bye" :
#                     print "exit from thread"
#                     return False



       
# class yaw_thread(threading.Thread):
#     """docstring for left_steps"""
#     def __init__(self, threadID):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#     def run(self):
#         global yaw,direc,error_num
#         while True:
#             error_num = error(int(yaw),direc)
#             #rospy.loginfo(error_num)
#             if stop == "bye" :
#                     print "exit from thread"
#                     return False


# def error(angle,dest_angle):
#     current = angle
#     target = dest_angle
#     temp = current 
#     origin = current - temp
#     transf_target = temp - target
#     if transf_target <= 180 :
#         errangle = transf_target
#     else: 
#         errangle = transf_target - 360
#     return int(errangle)    


# # class threadrun (threading.Thread):
# #     def __init__(self, threadID):
# #         threading.Thread.__init__(self)
# #         self.threadID = threadID
# #     def run(self):
# #         global stop,yaw
# #         while True :
# #             reading = serial_port.readline().decode()
# #             yaw = round(float(reading))
# #             # error_num = error(int(yaw),direc)
# #             rospy.loginfo("current yaw : "+reading)
# #             rospy.loginfo("direc yaw : "+str(direc))
# #             rospy.loginfo("error yaw : "+str(error_num))
# #             if stop == "bye":
# #                 print("thread")
# #                 serial_port.close()
# #                 return True


# def drivemode(data):
#     global drive_auto
#     if str(data.data) == "auto":
#         drive_auto = True
#         rospy.loginfo("systems online")
#     if str(data.data) == "manu":
#         drive_auto = False  


# def callback(data):
#     #rospy.loginfo(data.data)
#     global left_cmd,right_cmd,MOTOR_LEFT_DIR,MOTOR_RIGHT_DIR,left_bottom,right_bottom,drive_auto,direc,start_drive,left_inc,right_inc,right_finite,left_finite,error_num
#     if drive_auto == False : 
#         if str(data.data) == "up" :
#             rospy.loginfo("up")
#             left_bottom = 200
#             right_bottom = 200
#             left_cmd = 1
#             right_cmd = 1
#             GPIO.output(MOTOR_LEFT_DIR,1)
#             GPIO.output(MOTOR_RIGHT_DIR,0)
#         elif str(data.data) == "down" :
#             rospy.loginfo("down")
#             left_bottom = 200
#             right_bottom = 200
#             left_cmd = 1
#             right_cmd = 1
#             GPIO.output(MOTOR_LEFT_DIR,0)
#             GPIO.output(MOTOR_RIGHT_DIR,1)
#         elif str(data.data) == "right" :
#             rospy.loginfo("right")
#             left_bottom = 400
#             right_bottom = 400
#             left_cmd = 1
#             right_cmd = 1
#             GPIO.output(MOTOR_LEFT_DIR,1)
#             GPIO.output(MOTOR_RIGHT_DIR,1)
#         elif str(data.data) == "left" :
#             rospy.loginfo("left")
#             left_bottom = 400
#             right_bottom = 400
#             left_cmd = 1
#             right_cmd = 1
#             GPIO.output(MOTOR_LEFT_DIR,0)
#             GPIO.output(MOTOR_RIGHT_DIR,0)
#         elif str(data.data) == "rup" :
#             rospy.loginfo("rup")
#             left_cmd = 2
#             right_cmd = 2
#         elif str(data.data) == "rdown" :
#             rospy.loginfo("rdown")
#             left_cmd = 2
#             right_cmd = 2
#         elif str(data.data) == "rleft" :
#             rospy.loginfo("rleft")
#             left_cmd = 2
#             right_cmd = 2
#         elif str(data.data) == "rright" :
#             rospy.loginfo("rright")
#             left_cmd = 2
#             right_cmd = 2
#         elif str(data.data) == "stop":
#             rospy.loginfo("release")    
#             left_cmd = 2
#             right_cmd = 2
#     elif drive_auto == True :
#         if str(data.data) == "front":
#             left_bottom = 200
#             right_bottom = 200
#             left_cmd = 1
#             right_cmd = 1
#             GPIO.output(MOTOR_LEFT_DIR,1)
#             GPIO.output(MOTOR_RIGHT_DIR,0)
#         elif str(data.data) == "rfront":
#             left_cmd = 2
#             right_cmd = 2
#         elif str(data.data) == "back":
#             left_bottom = 200
#             right_bottom = 200
#             left_cmd = 1
#             right_cmd = 1
#             GPIO.output(MOTOR_LEFT_DIR,0)
#             GPIO.output(MOTOR_RIGHT_DIR,1)
#         elif str(data.data) == "rback":
#             left_cmd = 2
#             right_cmd = 2
#         else :
#             rospy.loginfo("here : " + str(data.data))
#             direc = int(data.data)
#             rospy.loginfo("the error is " + str(error_num))
#             left_bottom = 1000
#             right_bottom = 1000
#             left_cmd = 1
#             right_cmd = 1
#             while abs(error_num) >=5:
#                 if error_num < 0 : 
#                     GPIO.output(MOTOR_LEFT_DIR,1)
#                     GPIO.output(MOTOR_RIGHT_DIR,1)
#                 elif error_num > 0 :
#                     GPIO.output(MOTOR_LEFT_DIR,0)
#                     GPIO.output(MOTOR_RIGHT_DIR,0)
#             left_cmd = 2
#             right_cmd = 2
                




# def callyaw(data):
#     global yaw
#     yaw = round(data.data)
#     # rospy.loginfo(round(data.data))


# def myhook():
#     global stop
#     stop = "bye"
#     GPIO.cleanup()

# try :
#     # Create new threads
#     thread1 = left_thread(1)
#     thread2 = right_thread(1)
#     thread3 = left_steps(1)
#     thread4 = right_steps(1)
#     # thread = threadrun(1)
#     thread5 = yaw_thread(1)
#     # thread.start()
#     thread1.start()
#     thread2.start()
#     thread3.start()
#     thread4.start()
#     thread5.start()
#     rospy.init_node('drive_ctrl')
#     rospy.Subscriber("/simple_ctrl", String, callback)
#     rospy.Subscriber("/yaw", Float32, callyaw)
#     rospy.Subscriber("/drive_mode", String, drivemode)
#     rospy.on_shutdown(myhook)
#     rospy.spin()

# except (KeyboardInterrupt,rospy.ROSException):
#     stop = "bye"
#     GPIO.cleanup()



# @atexit.register
# def cleanup():
#     stop = "bye"
#     GPIO.cleanup()




#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import threading
import RPi.GPIO as GPIO
import time
import atexit

stop = ""

left_cmd = 3
left_inc = 800
left_top = 800
left_bottom = 200
left_finite = False
left_acc = 0.003

right_cmd = 3
right_inc = 800
right_top = 800
right_bottom = 200
right_finite = False
right_acc = 0.003

drive_auto = False
start_drive = False
direc = 0
yaw = 0
error_num = 0

#Pins definitions
MOTOR_LEFT_STEPS = 11
MOTOR_LEFT_DIR = 7
MOTOR_RIGHT_STEPS = 37
MOTOR_RIGHT_DIR = 35

#GPIO setup and init.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTOR_LEFT_STEPS, GPIO.OUT)
GPIO.setup(MOTOR_LEFT_DIR, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_STEPS, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_DIR, GPIO.OUT)

class left_thread (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global left_cmd,left_inc,left_top,left_bottom,left_finite,left_acc,stop
        while True :
            if left_cmd == 2 : # rising delay
                while True and stop != "bye" and left_inc < left_top:
                    if left_cmd == 2 : 
                        left_inc +=  3# print left_inc
                        time.sleep(left_acc)
                    else :
                        break 
                left_finite = False #stop drive
                if left_cmd == 2:
                    left_cmd = 3
                    pass
            if left_cmd == 1 : #falling delay
                left_finite = True #start drive
                while True and stop != "bye" and left_inc > left_bottom:
                    if left_cmd == 1: 
                        left_inc -=  3# print left_inc
                        time.sleep(left_acc)
                    else :
                        break   
                if left_cmd == 1:
                    left_cmd = 3
            if left_cmd ==3 :       
                time.sleep(left_acc)                
                if stop == "bye" :
                    print "exit from thread"
                    return False
            if stop == "bye" :
                print "exit from thread"
                return False



class right_thread (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global right_cmd,right_inc,right_top,right_bottom,right_finite,right_acc,stop
        while True :
            if right_cmd == 2 : # rising delay
                while True and stop != "bye" and right_inc < right_top:
                    if right_cmd == 2 : 
                        right_inc += 3  #print right_inc
                        time.sleep(right_acc)
                    else :
                        break 
                right_finite = False # stop drive           
                if right_cmd == 2:
                    right_cmd = 3
            if right_cmd == 1 : #falling delay
                right_finite = True # start drive
                while True and stop != "bye" and right_inc > right_bottom:
                    if right_cmd == 1: 
                        right_inc -=  3# print right_inc
                        time.sleep(right_acc)
                    else :
                        break   
                if right_cmd == 1:
                    right_cmd = 3    
            if right_cmd == 3 :
                time.sleep(right_acc)               
                if stop == "bye" :
                    print "exit from thread"
                    return False
                    
            if stop == "bye" :
                print "exit from thread"
                return False


class left_steps(threading.Thread):
    """docstring for left_steps"""
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global left_finite,left_inc,stop,MOTOR_LEFT_STEPS
        while True:
            while left_finite:
                GPIO.output(MOTOR_LEFT_STEPS,1)
                time.sleep(abs((left_inc)/1000000.0))
                GPIO.output(MOTOR_LEFT_STEPS,0)
                time.sleep(abs((left_inc)/1000000.0)) 
                if stop == "bye" :
                    print "exit from thread"
                    return False    
            if stop == "bye" :
                    print "exit from thread"
                    return False
                                
        
class right_steps(threading.Thread):
    """docstring for left_steps"""
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global right_finite,right_inc,stop,MOTOR_RIGHT_STEPS
        while True:
            while right_finite:
                GPIO.output(MOTOR_RIGHT_STEPS,1)
                time.sleep(abs(right_inc/1000000.0))
                GPIO.output(MOTOR_RIGHT_STEPS,0)
                time.sleep(abs(right_inc/1000000.0))  
                if stop == "bye" :
                    print "exit from thread"
                    return False
            if stop == "bye" :
                    print "exit from thread"
                    return False



def drivemode(data):
    global drive_auto
    if str(data.data) == "auto":
        drive_auto = True
        rospy.loginfo("systems online")
    if str(data.data) == "manu":
        drive_auto = False  


def callback(data):
    #rospy.loginfo(data.data)
    global left_cmd,right_cmd,MOTOR_LEFT_DIR,MOTOR_RIGHT_DIR,left_bottom,right_bottom,drive_auto,direc,start_drive,left_inc,right_inc,right_finite,left_finite
    if drive_auto == False : 
        if str(data.data) == "up" :
            rospy.loginfo("up")
            left_bottom = 200
            right_bottom = 200
            left_cmd = 1
            right_cmd = 1
            GPIO.output(MOTOR_LEFT_DIR,1)
            GPIO.output(MOTOR_RIGHT_DIR,0)
        elif str(data.data) == "down" :
            rospy.loginfo("down")
            left_bottom = 200
            right_bottom = 200
            left_cmd = 1
            right_cmd = 1
            GPIO.output(MOTOR_LEFT_DIR,0)
            GPIO.output(MOTOR_RIGHT_DIR,1)
        elif str(data.data) == "right" :
            rospy.loginfo("right")
            left_bottom = 600
            right_bottom = 600
            left_cmd = 1
            right_cmd = 1
            GPIO.output(MOTOR_LEFT_DIR,1)
            GPIO.output(MOTOR_RIGHT_DIR,1)
        elif str(data.data) == "left" :
            rospy.loginfo("left")
            left_bottom = 600
            right_bottom = 600
            left_cmd = 1
            right_cmd = 1
            GPIO.output(MOTOR_LEFT_DIR,0)
            GPIO.output(MOTOR_RIGHT_DIR,0)
        elif str(data.data) == "rup" :
            rospy.loginfo("rup")
            left_cmd = 2
            right_cmd = 2
        elif str(data.data) == "rdown" :
            rospy.loginfo("rdown")
            left_cmd = 2
            right_cmd = 2
        elif str(data.data) == "rleft" :
            rospy.loginfo("rleft")
            left_cmd = 2
            right_cmd = 2
        elif str(data.data) == "rright" :
            rospy.loginfo("rright")
            left_cmd = 2
            right_cmd = 2
        elif str(data.data) == "stop":
            rospy.loginfo("release")    
            left_cmd = 2
            right_cmd = 2
    elif drive_auto == True :
        if str(data.data) == "up" :
            rospy.loginfo("up")
            left_bottom = 500
            right_bottom = 500
            left_cmd = 1
            right_cmd = 1
            GPIO.output(MOTOR_LEFT_DIR,1)
            GPIO.output(MOTOR_RIGHT_DIR,0)
        elif str(data.data) == "down" :
            rospy.loginfo("down")
            left_bottom = 500
            right_bottom = 500
            left_cmd = 1
            right_cmd = 1
            GPIO.output(MOTOR_LEFT_DIR,0)
            GPIO.output(MOTOR_RIGHT_DIR,1)
        elif str(data.data) == "right" :
            rospy.loginfo("right")
            left_bottom = 1000
            right_bottom = 1000
            left_cmd = 1
            right_cmd = 1
            GPIO.output(MOTOR_LEFT_DIR,1)
            GPIO.output(MOTOR_RIGHT_DIR,1)
        elif str(data.data) == "left" :
            rospy.loginfo("left")
            left_bottom = 1000
            right_bottom = 1000
            left_cmd = 1
            right_cmd = 1
            GPIO.output(MOTOR_LEFT_DIR,0)
            GPIO.output(MOTOR_RIGHT_DIR,0)
        elif str(data.data) == "rup" :
            rospy.loginfo("rup")
            left_cmd = 2
            right_cmd = 2
        elif str(data.data) == "rdown" :
            rospy.loginfo("rdown")
            left_cmd = 2
            right_cmd = 2
        elif str(data.data) == "rleft" :
            rospy.loginfo("rleft")
            left_cmd = 2
            right_cmd = 2
        elif str(data.data) == "rright" :
            rospy.loginfo("rright")
            left_cmd = 2
            right_cmd = 2
        elif str(data.data) == "stop":
            rospy.loginfo("release")    
            left_cmd = 2
            right_cmd = 2

                


def rotate(where):
    global yaw,error_num
    if where == "left":
        while True:
            pass
    elif where == "right":
        pass
    return True


def error(angle,dest_angle):
    current = angle
    target = dest_angle
    temp = current 
    origin = current - temp
    transf_target = temp - target
    if transf_target <= 180 :
        errangle = transf_target
    else: 
        errangle = transf_target - 360
    return int(errangle)    


def callyaw(data):
    global yaw
    yaw = data.data
    rospy.loginfo(yaw)


def myhook():
    global stop
    stop = "bye"
    GPIO.cleanup()

try :
    # Create new threads
    thread1 = left_thread(1)
    thread2 = right_thread(1)
    thread3 = left_steps(1)
    thread4 = right_steps(1)
    # Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
  
    rospy.init_node('drive_ctrl')
    rospy.Subscriber("/simple_ctrl", String, callback)
    rospy.Subscriber("/yaw", Float32, callyaw)
    rospy.Subscriber("/drive_mode", String, drivemode)
    rospy.on_shutdown(myhook)
    rospy.spin()

except (KeyboardInterrupt,rospy.ROSException):
    stop = "bye"
    GPIO.cleanup()



@atexit.register
def cleanup():
    stop = "bye"
    GPIO.cleanup()

