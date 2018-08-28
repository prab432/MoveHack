#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
from sensor_msgs.msg import Imu
import geometry_msgs
import tf

def callback(data):
    quaternion = (
        data.orientation.x,
        data.orientation.y,
        data.orientation.z,
        data.orientation.w)
    euler = tf.transformations.euler_from_quaternion(quaternion)
    yaw = abs(-180+round((float(euler[2])*180)/3.14))
    pub.publish(yaw)


if __name__ == '__main__':
    try:
    	pub = rospy.Publisher('/yaw', Int16, queue_size=1, latch = False)
    	rospy.init_node('yaw_cal')
    	rospy.Subscriber("imu/data", Imu, callback)
    	rospy.spin()
    except rospy.ROSInterruptException:
        pass

