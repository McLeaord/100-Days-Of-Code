#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def shapes():
    rospy.init_node('shapes', anonymous=True)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)
    m = Twist()
    rate.sleep()
    
    for i in range(3):
         #front
        m.linear.x = 0.8
        m.angular.z = 2
        rospy.loginfo(m)
        pub.publish(m)
        rate.sleep()



if __name__=='__main__':
    shapes()