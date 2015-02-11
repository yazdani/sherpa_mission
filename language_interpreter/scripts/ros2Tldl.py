#!/usr/bin/env python

import rospy
import socket
from ros2Tldl.msg import language_interpreter
import sys
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard %s",data.data)

def listener():

    rospy.init_node('tldl_sub')
    rospy.Subscriber("chatter", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    
    print "hu"
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print "hu2"
    server_address = ("yazdani",1234)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    print "hu3"
    try: 
        print "hu4"
        while not rospy.is_shutdown():
            print "hu5"
            message = 'Go left.'
            if message:
                print "hu6"
                print >>sys.stderr, 'sending "%s"' % message
                sock.sendall(message)
            else:
                break
    except Exception, e:
        alert("Something strange happened with the connection")

    sock.shutdown(socket.SHUT_RDWR)
    print >>sys.stderr, 'closing socket'

    sock.close()


if __name__ == '__main__':
    listener()
