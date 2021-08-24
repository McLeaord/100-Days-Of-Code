#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Temperature

def publisher():
    rospy.init_node("publisher")
    pub=rospy.Publisher("HelloWorld",Temperature,queue_size=10)
    rate=rospy.Rate(1)
    a=Temperature()

    while not rospy.is_shutdown():
        a.temperature =10
        pub.publish(a)
        rate.sleep()


if __name__=="__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass




