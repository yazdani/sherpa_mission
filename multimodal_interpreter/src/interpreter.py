#!/usr/bin/env python

import socket, pickle
import rospy
import os, sys
import os.path
from std_msgs.msg import String
from multimodal_interpreter.msg import multimodal_msgs
from multimodal_interpreter.msg import response_msgs
from multimodal_interpreter.msg import multimodal_values

action=''
directive=''
cmd_typ=''
pub=''
#interpreted_cmd=''
#str1=''
agent=''
#dat=''
cmd_typ=''
#dire=''
#loc=''
#poly=''
#seg=''
#circ=''
pose=''
#artest=''
#artest2=''
item = ''
path = "/home/yazdani/work/ros/indigo/catkin_ws/src/iai_rescue_mission/instruct_mission/src/tmp"
outFile = "tmp.txt"
#commander=''

def callback(msg):
     global agent 
     global pose
     agent = msg.selected
     tmp = msg.command
     cmd = tmp.replace("_", " ")
     checkCmdType(cmd)
     checkAction(cmd)
     pose = msg.direction
     pose_tmp = str(pose).strip('[]')
     with open(path+"/"+outFile,'w') as o:
          o.write("agent: "+agent+"\n")
          o.write("action: "+action+"\n")
          o.write("type: "+cmd_typ+"\n")
          o.write("directive: "+directive+"\n")
          o.write("item: "+item+"\n")
          o.write("location: "+pose_tmp+"\n")
     pub.publish(agent,action,cmd_typ,directive,item,pose)

def checkCmdType(date):
     global cmd_typ
     data = date.split(" ")
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
          cmd_typ = "ask"
     else:
          cmd_typ = "order"
          

def checkAction(date):
     global action
     global directive
     global item
     tmp = date + '\n'
     c.send(tmp)
     sys.stdout.flush()
     interpreted_cmd = c.recv(1024)
     test1 = interpreted_cmd.split(")")
     test2 = test1[0].split('\n')
     test3 = test2[0].split("(")
     action = test3[0]
     print test3[0]
     print test3[1]
     directive = test3[1]
     if len(test3) > 2:
          item = test3[3]
     else:
          item = ''
    
   

def startConnection():
    global pub
    global c
    pub = rospy.Publisher('multimodal_msgs', multimodal_values, queue_size=10)
    rospy.init_node('multimodal')
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
     if os.path.exists(path):
          print "directory already exist"
     else:
          os.mkdir(path, 0755 );
     startConnection()
