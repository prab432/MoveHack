#!/usr/bin/env python
import rospy
from drive_ctrl.srv import angle
from std_msgs.msg import String
from std_msgs.msg import Int16  

yaw = 0 
offset = -5 #angle juggad

def callyaw(data):
    global yaw
    yaw = int(data.data)
    
    
def handle_angle(req):
    global yaw,offset
    pubbed = True
    if int(req.yaw) > yaw :
        rospy.loginfo("right")
        while yaw != int(req.yaw) - offset:
            if pubbed == True:
                drive_pub.publish("right")
                pubbed = False
        drive_pub.publish("rright")
    elif int(req.yaw) < yaw :
        rospy.loginfo("left")
        while yaw != int(req.yaw) + offset:
            if pubbed == True:
                drive_pub.publish("left")        
                pubbed = False 
        drive_pub.publish("rleft")
    return True
        
# def handle_diff(req):
   
#     if req.direc==1:   
#         pubbed = True
#         target=(yaw+req.yaw)%360
#         diff=(target-yaw)%360 - offset
#         prev=yaw   
#         while diff>0:
#           diff-=(yaw-prev)%360
#           rospy.loginfo("right : " + str(diff))
#           prev=yaw
#           if pubbed == True:
#              drive_pub.publish("right")
#              pubbed = False
#         drive_pub.publish("rright")
#     elif req.direc==0:
#         pubbed = True
#         target=(yaw-req.yaw)%360
#         diff=(yaw-target)%360 - offset
#         prev=yaw
#         while diff>0:
#           rospy.loginfo("left : " + str(diff))
#           diff-=(prev-yaw)%360
#           prev=yaw
#           if pubbed == True:
#              drive_pub.publish("left")
#              pubbed = False
#         drive_pub.publish("rleft")
#     return True

def handle_diff(req):
    global yaw,offset
    if req.direc==1: #forr
        pubbed=True
        target=(yaw+req.yaw)%360 - offset
        while(yaw-target)%360 < 350:    
            if pubbed==True:
                drive_pub.publish("right")
                # rospy.loginfo("RIGHT:", str(((yaw-target)%360)))
                pubbed=False
        drive_pub.publish("rright")

    if req.direc==0:
        pubbed=True
        target=(yaw-req.yaw)%360 + offset
        while(target-yaw)%360 < 350:
            if pubbed==True:
                drive_pub.publish("left")
                # rospy.loginfo("left:", str(((yaw-target)%360)))
                pubbed=False
        drive_pub.publish("rleft")

    return True




            
    
        

if __name__ == "__main__":
    drive_pub = rospy.Publisher('/simple_ctrl', String, queue_size=1)
    rospy.init_node('angle_server')
    rospy.Subscriber("/yaw", Int16, callyaw)
    s = rospy.Service('angle', angle, handle_angle)
    s1 = rospy.Service('anglediff', angle, handle_diff)
    rospy.spin()
