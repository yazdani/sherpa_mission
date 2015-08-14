#!/usr/bin/env python

import socket, pickle
import rospy
from std_msgs.msg import String
import sys

pub=''
str2=''
str1=''
def callback(date):
     print "moin"
     global str2
     tmp = date.data + '\n'
     print tmp
     
     c.send(tmp)
     sys.stdout.flush()
     str2 = c.recv(1024)
     pub.publish(str2)

def interpret():
    global pub
    global c
    rospy.init_node('tf_transforms2')
    pub = rospy.Publisher('multimodal_interpreter', String, queue_size=10)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("yazdani", 1234))
    s.listen(1)
    server = "yazdani"
    c, address = s.accept()
    rospy.Subscriber("test_msgs", String, callback)
    rospy.spin()
    s.shutdown(socket.SHUT_RDWR)
    s.close()

if __name__ == '__main__':
    interpret()
