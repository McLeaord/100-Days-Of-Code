#! /usr/bin/python3

import rospy
from std_msgs.msg import String
from rmp08.msg import tdpll

def callback(data):
    print()
    print("***************************************")
    print("      START        ")
    print("PLACE : ",data.place)
    print()
    print("TEMPERATURE : ",data.Temperature)
    print()
    print("X : ",data.x)
    print("Y : ",data.y)
    print()
    print("DISTANCE IS : ",data.distance)
    print("      END      ")
    print("***************************************")
    print()

def listen():
    rospy.init_node("subscriber",anonymous=True)
    rospy.Subscriber("talking",tdpll,callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        listen()
    except rospy.ROSInterruptException:
        pass