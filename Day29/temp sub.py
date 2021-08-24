#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Temperature


def callback(msg):
    print(msg.temperature)



if __name__=="__main__":
    rospy.init_node("subscriber")
    rospy.Subscriber("HelloWorld",Temperature,callback)
    rospy.spin()
 