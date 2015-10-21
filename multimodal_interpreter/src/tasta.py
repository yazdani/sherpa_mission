#!/usr/bin/env python

import socket, pickle
import rospy
from std_msgs.msg import String
from multimodal_interpreter.msg import multistring
from multimodal_interpreter.msg import multistrings
import os, sys
import os.path


path = "/home/yazdani/work/ros/indigo/catkin_ws/src/iai_rescue_mission/startup_mission/src/tmp"

outFile = "tmp.txt"



def startSocket():
    pub = rospy.Publisher('checker2', String, queue_size=10)
    rospy.init_node('tf_transforms')
    rate = rospy.Rate(0.1)
    hello_str =  multistring()
    array = []
    stering = ""
    artest = multistring()
    artest2 = "moinsen"
    testpath = ''
    i = 0
    while not rospy.is_shutdown():
        artest.agent = "mo"
        artest.command = "am"
        artest.command_type = "mu"
        i = i + 1
        with open(path+"/"+outFile,'w') as o:
            o.write(artest2 +" "+str(i))
            testpath = path+"/"+outFile
        pub.publish(artest2)
        rate.sleep()
        artest = multistring()
        f = open(path+"/"+outFile,'r+')
        print "test"
        f.truncate()
    os.remove(path+"/")
    print "removed"

    

if __name__ == '__main__':
    if os.path.exists(path):
        print "directory already exist"
    else:
        os.mkdir( path, 0755 );
    startSocket()



