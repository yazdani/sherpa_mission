#!/usr/bin/env python
# license removed for brevity

__author__= 'Fereshta Yazdani'

import rospy
import roslib
import xml.etree.ElementTree as ET 
from language_interpreter.msg import StringMultiArrays
from language_interpreter.msg import StringMultiArray
import tf
import os
import geometry_msgs.msg
import std_msgs.msg
import language_interpreter.msg

array = []

def main():
   
    global pub1
    rospy.init_node('HRI_command')
    pub1 = rospy.Publisher('intern_call',language_interpreter.msg.StringMultiArrays , queue_size=10)
    rospy.Subscriber("HRIOut", std_msgs.msg.String, callback)
    rospy.spin()

def callback(data):
    ar2 = StringMultiArrays()
    ar1 = StringMultiArray()
    print type(ar2)
    array = []
    #Reading the data from a string
    root = ET.fromstring(data.data)

    for child in root:
        for child2 in child:
                child3 = child2.tag
                child4 = child3.split("}")
                array.append([child4[1], child2.text])
   
    if len(array) == 4:
        array.append(["blank", "blank"])
    ar1.str1 = array[0]
    ar1.str2 = array[1]
    ar1.str3 = array[2]
    ar1.str4 = array[3]
    ar1.str5 = array[4]
    ar2.multi.append(ar1)
  
    pub1.publish(ar2)
  
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
