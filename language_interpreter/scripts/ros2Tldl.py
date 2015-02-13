#!/usr/bin/env python

import socket
import rospy
from language_interpreter.msg import ros2Tldl 
import sys
from std_msgs.msg import String

iterator = []

def buffer(data):
    #TODO: Really bad solution
    iterator.append(data)
    if data:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_address = ("yazdani",1234)
        # print >>sys.stderr, 'connecting to %s port %s' % server_address
        sock.connect(server_address)
        sock.send(iterator[0])
        iterator.pop(0)
        sock.shutdown(socket.SHUT_RDWR)
        # print >>sys.stderr, 'closing socket'      
        sock.close()
    else:
        print("")

def callback(data):
    buffer(data.data) 
    rospy.loginfo(data.data)
   
  
def listener():   
    rospy.init_node('ros2Tldl_pub')
    rospy.Subscriber("tldl_tester", String, callback)
    rospy.spin()    
  

if __name__ == '__main__':
    listener()
