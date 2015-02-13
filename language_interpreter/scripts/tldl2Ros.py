#!/usr/bin/env python

__author__= 'Fereshta Yazdani'

import socket
import rospy
from language_interpreter.msg import tldl2Ros
import os
import string

SERVER = 'yazdani'
BUFSIZE = 4096

# def getch():
#      os.system("bash -c \"read -n 1\"")

def TLDL_publisher():
    
    pub = rospy.Publisher('tldl2Ros', tldl2Ros, queue_size=10)
    rospy.init_node('tldl2Ros')
    msg= tldl2Ros()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("yazdani", 4321))
    s.listen(1)
    server = "yazdani"
    try: 
         conn = s.accept()
         daty = conn[0]
         while not rospy.is_shutdown():
              data = daty.recv(4096)
              if data:
                pub.publish(data)
                print(data)
              else:
                break
         # getch()
    except Exception, e:
         alert("Something strange happened with the connection")

    s.shutdown(socket.SHUT_RDWR)
    s.close()

if __name__ == '__main__':
    TLDL_publisher()
