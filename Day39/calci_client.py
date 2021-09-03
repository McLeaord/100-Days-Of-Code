#!/usr/bin/python3

from rmp08.srv import calci
from rmp08.srv import calciRequest
from rmp08.srv import calciResponse
import rospy
import sys
def calci_client(x,y,op):
    rospy.init_node('client_node',anonymous=True)
    rospy.wait_for_service('calci',timeout=40)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            client=rospy.ServiceProxy('calci',calci)
            response=client(x,y,op)
            rospy.loginfo(response.result)
            return response.result
        except rospy.ServiceException as e:
            print("SERVICE FAILED %s"%e)


if __name__=="__main__":

    x=int(input("ENTER THE FIRST NUMBER:"))
    y=int(input("ENTER THE SECOND NUMBER"))
    op=input("ENTER THE OPERATION")


    print("REQUESTING ")
    result=calci_client(x,y,op)
    print("RESULT=%s"%result)