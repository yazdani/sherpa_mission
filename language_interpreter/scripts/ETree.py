#!/usr/bin/env python
# license removed for brevity

__author__= 'Fereshta Yazdani'

import rospy
import roslib
import xml.etree.ElementTree as ET 
from language_interpreter.msg import MultiStrArray
import tf
import os
import geometry_msgs.msg
import std_msgs.msg

array1 = []
pub1 = []

def main():
    global pub1
    rospy.init_node('HRI_command')
    pub1 = rospy.Publisher('intern_call',MultiStrArray , queue_size=10)
    rospy.Subscriber("HRIOut", std_msgs.msg.String, callback)
    rospy.spin()

def callback(data):
    global array1
    global tmp1, tmp2
    #Reading the data from a string
    root = ET.fromstring(data.data)
    for child in root:
        for child2 in child:
            child3 = child2.tag
            child4 = child3.split("}")
            tmp1 = child4[1]
            tmp2 = child2.text
            array1.append(tmp1)
            array1.append(tmp2)
    pub1.publish(array1)
    array1 = []

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
