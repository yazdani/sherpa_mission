#!/usr/bin/env python

import socket, pickle
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
c_test = 0
tr1 = 0
tr2 = 0
pub = 0
def socket_con(date):  
    global str2
   # digit1 = date.str
    digit = date + '\n'
    #digit = date
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
        
def callback():
    socket_conTest()
    pub.publish(str1, str2, tr1, tr2)
    
    
def socket_conTest():
    global tr1
    global tr2
    c_test.send("ok\n")
    sys.stdout.flush()
    data = c_test.recv(1024)
    date = pickle.loads(data)
    tr1 = date[1]
    tr2 = date[2]
    socket_con(date[0])    
    check_com(date[0])
    
    
def connector():
    print "connector"
    global c
    global c_test
    global pub
    rospy.init_node('tf_transforms')
    pub = rospy.Publisher('interpreted_command',tldl2Ros, queue_size=10)
    s_test = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s_test.bind(("yazdani", 5678))
    s_test.listen(1)
    c_test,address_test = s_test.accept()
    print "first connection"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("yazdani", 1234))
    s.listen(1)
    server = "yazdani"
    c, address = s.accept()
    print "second connection"
    while True:
        callback()
       
        # rospy.Subscriber("multimodal_command", testmsg, callback)
        # rospy.spin()
     
    s.shutdown(socket.SHUT_RDWR)
    s.close()
    s_test.shutdown(socket.SHUT_RDWR)
    s_test.close()  
    
if __name__ == '__main__':
    connector()
 