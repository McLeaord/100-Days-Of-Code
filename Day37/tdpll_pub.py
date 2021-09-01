#! /usr/bin/python3

import rospy
from std_msgs.msg import String
from rmp08.msg import tdpll

def talk():
    pub=rospy.Publisher("talking",tdpll,queue_size=10)
    rospy.init_node("publisher",anonymous=True)
    rate=rospy.Rate(1)
    rospy.loginfo("publishing messages started")
    while not rospy.is_shutdown():
        msg=tdpll()
        msg.place="IN MAZE"
        msg.Temperature=90
        msg.distance=50
        msg.x=2.0
        msg.y=3.0
        pub.publish(msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        talk()
    except rospy.ROSInterruptException:
        pass