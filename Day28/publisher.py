#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def dennis():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('dennis', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "dennis here %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        dennis()
    except rospy.ROSInterruptException:
        pass