#!/usr/bin/env python3

import rospy
from rmp08.srv import multiplier,multiplierResponse

def callback(request):
    return multiplierResponse(request.a * request.b)

def multiply():
    rospy.init_node("multiplier_service")
    service=rospy.Service("multiplication",multiplier,callback)
    rospy.spin()

if __name__ == "__main__":
    multiply()