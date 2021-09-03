#!/usr/bin/python3

import rospy
from rmp08.srv import calci
from rmp08.srv import calciRequest
from rmp08.srv import calciResponse


def caliculator (nb1, nb2, op):
    result = 0 
    
    if  op =='+':
        result=nb1+nb2
        
    elif op=='-':
        result=nb1-nb2
       
    elif op=='*':
        result=nb1*nb2
        
    elif op=='/':
        try:
            result=nb1/nb2
            
        except ZeroDivisionError:
            result="Can’t divide by 0"
    
    return result

def callback(req):
    result = 0
    
    if  str(req.symbol)=='+':
        result=req.a+req.b
        
    elif str(req.symbol)=='-':
        result=req.a-req.b
       
    elif str(req.symbol)=='*':
        result=req.a*req.b
        
    elif str(req.symbol)=='/':
        
        try:
            result=req.a/req.b
            
        except ZeroDivisionError:
            result="Can’t divide by 0"
    
    return calciResponse(result)
    
def calculate():
    rospy.init_node('Calculator')
    s= rospy.Service('calci',calci,callback)
    print("calculator started")
    rospy.spin()

if __name__=="__main__":
    calculate()