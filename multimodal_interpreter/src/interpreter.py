#!/usr/bin/env python

import socket, pickle
import rospy
from std_msgs.msg import String
from multimodal_interpreter.msg import multimodal_msgs
from multimodal_interpreter.msg import response_msgs
import sys

pub=''
str2=''
str1=''
sel=''
dat=''
typ=''
dire=''
loc=''
poly=''
seg=''
circ=''
pose=''


def callback(date):
     declareVariables(date)
     tmp = date.command
     rplace = tmp.replace("_", " ")
     checkCommandType(rplace)
     sendSocket(rplace)


def declareVariables(date):
     global sel
     global dat
     global dire
     global loc
     global poly
     global seg
     global circ
     global pose
     sel = date.selected
     dat = date.data
     dire = date.direction
     loc = date.location
     poly = date.polygonal_area
     seg = date.segment
     circ = date.circ_area
     pose = date.sample


def checkCommandType(date):
     global typ
     typ = date 
     data = typ.split(" ")
     a = ''.join(['a', 'r', 'e'])
     b = ''.join(['d', 'o'])
     c = ''.join(['d', 'o', 'e', 's'])
     d = ''.join(['h', 'a', 'v', 'e'])
     e = ''.join(['h', 'a', 's'])
     f = ''.join(['h', 'o', 'w'])
     g = ''.join(['w', 'h', 'a', 't'])
     h = ''.join(['w', 'h', 'i', 'c', 'h'])
     i = ''.join(['w', 'h', 'e', 'r', 'e'])
     j = ''.join(['w', 'h', 'o'])
     k = ''.join(['w', 'h', 'o', 's', 'e'])
     l = ''.join(['w', 'h', 'y'])
     
     
     if data[0] == a or data[0] == b or data[0] == c or data[0] == d or data[0] == e or data[0] == f or data[0] == g or data[0] == h or data[0] == i or data[0] == j or data[0] == k or data[0] == l:
          typ = "ask"
     else:
          typ = "order"
          

def sendSocket(date):
     global str2
     tmp = date + '\n'
     c.send(tmp)
     sys.stdout.flush()
     str2 = c.recv(1024)
     pub.publish(sel, str2, typ, dat, dire, loc, poly, seg, circ, pose)


def startSocket():
    global pub
    global c
    pub = rospy.Publisher('multimodal_msgs', response_msgs , queue_size=10)
    rospy.init_node('tf_transforms2')
    rate = rospy.Rate(10)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("yazdani", 1234))
    s.listen(1)
    server = "yazdani"
    c, address = s.accept()
    rospy.Subscriber("test_msgs", multimodal_msgs, callback)
    rospy.spin()
    s.shutdown(socket.SHUT_RDWR)
    s.close()

if __name__ == '__main__':
    startSocket()
