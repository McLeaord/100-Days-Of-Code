#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
import math

def sensor(msg):
    print()
    print("*******************************************")
    print("      STARTING   ")
    print()
    print("MINIMUM ANGLE IS  :  ",math.degrees(msg.angle_min))
    print()
    print("MAXIMUM ANGLE IS  :  ",math.degrees(msg.angle_max))
    print()
    print("MAXIMUM RANGE IS  :  ",msg.range_max)
    print()
    print("RANGE AT 0 IS     :  ",msg.ranges[0])
    print()
    print("RANGE AT 90 IS    :  ",msg.ranges[90])
    print()
    print("RANGE AT 180 IS   :  ",msg.ranges[180])
    print()
    print("RANGE AT 270 IS   :  ",msg.ranges[270])
    print()
    print("   END    ")
    print("*******************************************")

if __name__ == "__main__":
    rospy.init_node("scanning")
    rospy.Subscriber("/scan",LaserScan,sensor)
    rospy.spin()