#!/usr/bin/env python

import socket
import rospy
from language_interpreter.msg import testmsg
from language_interpreter.msg import checkmsg
from language_interpreter.msg import tldl2Ros
import sys
import std_msgs.msg 
import geometry_msgs.msg

str2 = 0
str1 = 0
c = 0
sock = 0
def socket_con(date):  
    global str2
    digit1 = date.str
    digit = date.str + '\n'
    if digit:
        c.send(digit)
        sys.stdout.flush()
        str2 = c.recv(1024)
     
    else:
        print("")


def check_com(date):
    global str1
    str1 = date 
    data = str1.split(" ")
    a = ''.join(['A', 'r', 'e'])
    b = ''.join(['D', 'o'])
    c = ''.join(['D', 'o', 'e', 's'])
    d = ''.join(['H', 'a', 'v', 'e'])
    e = ''.join(['H', 'a', 's'])
    f = ''.join(['H', 'o', 'w'])
    g = ''.join(['W', 'h', 'a', 't'])
    h = ''.join(['W', 'h', 'i', 'c', 'h'])
    i = ''.join(['W', 'h', 'e', 'r', 'e'])
    j = ''.join(['W', 'h', 'o'])
    k = ''.join(['W', 'h', 'o', 's', 'e'])
    l = ''.join(['W', 'h', 'y'])


    if data[0] == a or data[0] == b or data[0] == c or data[0] == d or data[0] == e or data[0] == f or data[0] == g or data[0] == h or data[0] == i or data[0] == j or data[0] == k or data[0] == l:
        str1 = "ask"
    else:
        str1 = "order"

def callback(data):
    pub = rospy.Publisher('interpreted_command',tldl2Ros, queue_size=10)
    socket_con(data)
    check_com(data.str)
    pub.publish(str1, str2, data.transform1, data.transform2)

def connector():
    global  c
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("yazdani", 1234))
    s.listen(1)
    server = "yazdani"
    c, address = s.accept()
    rospy.init_node('tf_transforms')
    rospy.Subscriber("multimodal_command", testmsg, callback)
    rospy.spin()

    s.shutdown(socket.SHUT_RDWR)
    s.close()  

if __name__ == '__main__':
    connector()
 
