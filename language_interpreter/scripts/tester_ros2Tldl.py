#!/usr/bin/env python
# license removed for brevity

__author__= 'Fereshta Yazdani'

import socket
import rospy
import os
import string
from std_msgs.msg import String

def tester():
    pub = rospy.Publisher('tldl_tester',String , queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) 
    while not rospy.is_shutdown():
        hello_str1 = "Go left!"
        hello_str2 = "Go right!"
        hello_str3 = "Go straight!"
        hello_str4 = "Come back!"
        hello_str5 = "Go straight!" 
        hello_str6 = "Go forward!" 
        hello_str7 = "Go right!" 
        hello_str8 = "Go left!" 
        hello_str9 = "Go straight!" 
        hello_str10 = "Go left!" 
        hello_str11 = "Go right!"
        hello_str12 = "Go left!" 
        hello_str13 = "Go straight!" 
        rospy.loginfo(hello_str1)
        pub.publish(hello_str1)
        rate.sleep()
        rospy.loginfo(hello_str2)
        pub.publish(hello_str2)
        rate.sleep()
        rospy.loginfo(hello_str3)
        pub.publish(hello_str3)
        rate.sleep()
        rospy.loginfo(hello_str4)
        pub.publish(hello_str4)
        rate.sleep()        
        rospy.loginfo(hello_str5)
        pub.publish(hello_str5)
        rate.sleep()        
        rospy.loginfo(hello_str6)
        pub.publish(hello_str6)
        rate.sleep()        
        rospy.loginfo(hello_str7)
        pub.publish(hello_str7)
        rate.sleep()        
        rospy.loginfo(hello_str8)
        pub.publish(hello_str8)
        rate.sleep()        
        rospy.loginfo(hello_str9)
        pub.publish(hello_str9)
        rate.sleep()        
        rospy.loginfo(hello_str10)
        pub.publish(hello_str10)
        rate.sleep()        
        rospy.loginfo(hello_str11)
        pub.publish(hello_str11)
        rate.sleep()        
        rospy.loginfo(hello_str12)
        pub.publish(hello_str12)
        rate.sleep()       
        rospy.loginfo(hello_str13)
        pub.publish(hello_str13)
        rate.sleep()

if __name__ == '__main__':
    try:
        tester()
    except rospy.ROSInterruptException:
        pass
