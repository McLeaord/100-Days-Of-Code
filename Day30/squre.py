#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def square():
    rospy.init_node('square')
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)
    m = Twist()
    rate.sleep()
    
    for i in range(1):
         #front
        m.linear.x = 2
        m.angular.z = 0
        rospy.loginfo(m)
        pub.publish(m)
        rate.sleep()

        #stop
        m.linear.x = 0
        m.angular.z = 0
        rospy.loginfo(m)
        pub.publish(m)
        rate.sleep()

        #rotate
        m.linear.x = 0
        m.angular.z = 1.57
        rospy.loginfo(m)
        pub.publish(m)
        rate.sleep()
       
    
        
        #front
        m.linear.x = 2
        m.angular.z = 0
        rospy.loginfo(m)
        pub.publish(m)
        rate.sleep()

        

        #stop
        m.linear.x = 0
        m.angular.z = 0
        rospy.loginfo(m)
        pub.publish(m)
        rate.sleep()

        #rotate
        m.linear.x = 0
        m.angular.z = 1.57
        rospy.loginfo(m)
        pub.publish(m)
        rate.sleep()

         #front
        m.linear.x = 2
        m.angular.z = 0
        rospy.loginfo(m)
        pub.publish(m)
        rate.sleep()

    
        #stop
        m.linear.x = 0
        m.angular.z = 0
        rospy.loginfo(m)
        pub.publish(m)
        rate.sleep()

        #rotate
        m.linear.x = 0
        m.angular.z = 1.57
        rospy.loginfo(m)
        pub.publish(m)
        rate.sleep()


         #front
        m.linear.x = 2
        m.angular.z = 0
        rospy.loginfo(m)
        pub.publish(m)
        rate.sleep()

        #stop
        m.linear.x = 0
        m.angular.z = 0
        rospy.loginfo(m)
        pub.publish(m)
        rate.sleep()




        






if __name__=='__main__':
    square()
