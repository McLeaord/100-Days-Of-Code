#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


def callback(msg):
    print(msg.linear.x)
    print(msg.angluar.z)


if __name__=="__main__":
    rospy.init_node("subscriber")
    rospy.Subscriber("HelloWorld",Twist,callback)
    rospy.spin()
 