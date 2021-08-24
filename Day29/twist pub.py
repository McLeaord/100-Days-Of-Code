#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def publisher():
    rospy.init_node("publisher")
    pub=rospy.Publisher("HelloWorld",Twist,queue_size=10)
    rate=rospy.Rate(1)
    a=Twist()

    while not rospy.is_shutdown():
        a.linear.x =10
        a.angular.z =20
        pub.publish(a)
        rate.sleep()


if __name__=="__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass




