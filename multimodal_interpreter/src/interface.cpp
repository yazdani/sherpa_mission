#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
//#include <hector_quadrotor_msgs/followerAction.h>
#include <geometry_msgs/Pose.h>
#include <geometry_msgs/PoseStamped.h>
#include <geometry_msgs/Twist.h>
#include <gazebo_msgs/GetModelState.h>
#include <gazebo_msgs/SetModelState.h>
#include <geometry_msgs/Twist.h>
#include <sstream>
#include <multimodal_interpreter/multimodal_values.h>
#include "multimodal_interpreter/response_msgs.h"
#include "multimodal_interpreter/multimodal_msgs.h"
#include <string>
#include <std_msgs/String.h>
#include <iostream>
#include <tf/LinearMath/Quaternion.h>
#include <stdio.h> 
#include <math.h>
#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <sstream>

#define PORT
#define MAX_QUEUE 1
#define BUF_SIZE 1024


std_msgs::String msg;
std::stringstream ss;
geometry_msgs::Pose pose;
geometry_msgs::Point position;
geometry_msgs::Quaternion orientation;
multimodal_interpreter::multimodal_values multi;

ros::Publisher c_pub;

/*void startSocket()
{
int sock1, sock2;
chat buf_size[BUF_SIZE];
struct sockaddr_in server;
sock1 = socket(AF_INET,SOCK_STREAM,0);
if(sock1 < 0)
  {
perror("open stream socket");
exit(1);
}
server.sin_family = AF_INET;
server.sin_addr.s_addr =


}*/
using namespace std;


void splitter(std_msgs::String data)
{
  
  std_msgs::String word;
  std::vector<std_msgs::String> vec;
  for(unsigned i=1; i<data.length(); i++)
    {
      if(data.at(i) == "(" || data.at(i) == ")" || data.at(i) == "," )
	{
	  
	  std::cout << "nothing" << std::endl;
	  vec.push_back(word);
	   std_msgs::String word;
	}else
	{
	  word = word + data.at(i); 
	    }
    }}
  
  

/**
 * This tutorial demonstrates simple receipt of messages over the ROS system.
 */
void callback(const multimodal_interpreter::response_msgs::ConstPtr& msg)
{
  ROS_INFO("I heard:");
  std::cout << msg->selected << std::endl;
  multi.agent = msg->selected;
  multi.action = msg->command;
  multi.type = msg->type;
  multi.directive = msg->type;
  splitter(msg->command);

    position.x = 1.0;
    position.y = 2.0;
    position.z = 3.0;
  
    orientation.x = 3.0;
    orientation.y = 2.0;
    orientation.z = 1.0;
    orientation.w = 1.0;
    pose.position = position;
    pose.orientation = orientation;
    splitter(msg->command);
   multi.location = pose;
    ROS_INFO("I hefffard:");
   
    c_pub.publish(multi);
}













int main(int argc, char **argv)
{


ros::init(argc, argv, "multimodal_node");

/**
 * NodeHandle nh: for the publisher.
 * NodeHandle n: for the subscriber.
 */
ros::NodeHandle nh;
ros::NodeHandle n;

c_pub = nh.advertise<multimodal_interpreter::multimodal_values>("CMDtalker", 1000);

//startSocket();

ros::Subscriber sub = n.subscribe("multimodal_msgs", 1000, callback);

/**
 * ros::spin() will enter a loop, pumping callbacks.  With this version, all
 * callbacks will be called from within this thread (the main one).  ros::spin()
   * will exit when Ctrl-C is pressed, or the node is shutdown by the master.
   */
ros::spin();

return 0;
}


