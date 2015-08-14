#!/usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
   
    pub = rospy.Publisher('test_msgs', String, queue_size=10)
    rospy.init_node('tf_transforms')
    rate = rospy.Rate(40) 
    while not rospy.is_shutdown():
        hello_str = "Go right of this tree"
        pub.publish(hello_str)
        rate.sleep()