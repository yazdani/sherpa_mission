#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include <uav_controller/cmdVel.h>
#include <geometry_msgs/Pose.h>
#include <geometry_msgs/PoseStamped.h>
#include <geometry_msgs/Twist.h>
#include <gazebo_msgs/GetModelState.h>
#include <gazebo_msgs/SetModelState.h>
#include <geometry_msgs/Twist.h>
#include <sstream>
#include <string>
#include <std_msgs/String.h>
#include <iostream>
#include <tf/LinearMath/Quaternion.h>
#include <stdio.h> 
#include <math.h>

class cmdVel
{
protected:

  ros::NodeHandle nh_;
  ros::NodeHandle nh;
  actionlib::SimpleActionServer<uav_controller::cmdVel> action_; 
  std::string action_name_;
  hector_quadrotor_msgs::cmdVelFeedback feedback_;
  hector_quadrotor_msgs::cmdVelResult result_;
  ros::ServiceClient gms_c;  
  gazebo_msgs::SetModelState setmodelstate;
  gazebo_msgs::GetModelState getmodelstate; 
  ros::Publisher publisher;
  ros::ServiceClient smsl;
  geometry_msgs::Pose end_pose;
  geometry_msgs::Twist end_twist;

public:

 cmdVel(std::string name) :
    action_(nh_, name, boost::bind(&cmdVel::executeCB, this, _1), false),
    action_name_(name)
  {
    action_.start();
      ROS_INFO("Waiting for the Client to start the process");
  }

  ~cmdVel(void)
  {
  }

  void executeCB(const uav_controller::cmdVelGoalConstPtr &goal)
  {
    ROS_INFO("Client is registered, lets start the executing");
    publisher = nh.advertise<geometry_msgs::Twist>("cmd_vel", 1);
    gms_c = nh_.serviceClient<gazebo_msgs::GetModelState>("/gazebo/get_model_state");
    getmodelstate.request.model_name="quadrotor";

    geometry_msgs::Twist tw;
    publisher.publish(tw);
    ros::Duration(5.0).sleep();
    
    gms_c.call(getmodelstate);
    double now_x =  getmodelstate.response.pose.position.x;
    double now_y =  getmodelstate.response.pose.position.y;
    double now_z =  getmodelstate.response.pose.position.z;
    
    double new_x = goal->goal.position.x;
    double new_y = goal->goal.position.y;
    double new_z = goal->goal.position.z;

    double x_diff, y_diff, z_diff;
    double tmp_x, tmp_y, tmp_z;
    double var_x, var_y, var_z;

    ros::Rate r(1);
    bool success = true;
      
    ROS_INFO("%s: Executing!", action_name_.c_str());
        
    if (action_.isPreemptRequested() || !ros::ok())
      {
	ROS_INFO("%s: Preempted", action_name_.c_str());
	action_.setPreempted();
	success = false;
	//break;
      }
    
    publisher.publish(tw);
    ros::Duration(2.0).sleep();
       
    
    x_diff=new_x - now_x;
    y_diff=new_y - now_y; 
    z_diff=new_z - now_z;
    
    ROS_INFO(" Come Up Hector! ");
   
      
    publisher.publish(tw);
    ros::Duration(2.0).sleep();
    // tw.angular.z = -0.5;
    tw.linear.z = 0;
    tw.linear.x = 0;
    tw.linear.y = 0;

    publisher.publish(tw);
    ros::Duration(2.0).sleep();	
    ROS_INFO(" Good Boy, let's go further! ");
    
    while(now_z < new_z)
      {
	tw.linear.z = now_z * 0.1;
	publisher.publish(tw);
	ros::Duration(2.0).sleep();
	gms_c.call(getmodelstate);
	now_z =  getmodelstate.response.pose.position.z;
      }
    ros::Duration(2.0).sleep();
    tw.linear.z = 0;
    tw.linear.x = 0;
    tw.linear.y = 0;
    publisher.publish(tw);
    
    while(now_z > new_z)
      {
	tw.linear.z = now_z * -0.1;
	publisher.publish(tw);
	ros::Duration(2.0).sleep();
	gms_c.call(getmodelstate);
	now_z =  getmodelstate.response.pose.position.z;
      }

    ros::Duration(2.0).sleep();
    tw.linear.z = 0;
    tw.linear.x = 0;
    tw.linear.y = 0;
    publisher.publish(tw);


   while(now_x < new_x)
      {
	tw.linear.x = now_x * 0.1;
	publisher.publish(tw);
	ros::Duration(2.0).sleep();
	gms_c.call(getmodelstate);
	now_x =  getmodelstate.response.pose.position.x;
      }
    ros::Duration(2.0).sleep();
    tw.linear.z = 0;
    tw.linear.x = 0;
    tw.linear.y = 0;
    publisher.publish(tw);
    
    while(now_x > new_x)
      {
	tw.linear.x = now_x * -0.1;
	publisher.publish(tw);
	ros::Duration(2.0).sleep();
	gms_c.call(getmodelstate);
	now_x =  getmodelstate.response.pose.position.x;
      }

    ros::Duration(2.0).sleep();
    tw.linear.z = 0;
    tw.linear.x = 0;
    tw.linear.y = 0;
    publisher.publish(tw);

  while(now_y < new_y)
      {
	tw.linear.y = now_y * 0.1;
	publisher.publish(tw);
	ros::Duration(2.0).sleep();
	gms_c.call(getmodelstate);
	now_y =  getmodelstate.response.pose.position.y;
      }
    ros::Duration(2.0).sleep();
    tw.linear.z = 0;
    tw.linear.x = 0;
    tw.linear.y = 0;
    publisher.publish(tw);
    
    while(now_y > new_y)
      {
	tw.linear.y = now_y * -0.1;
	publisher.publish(tw);
	ros::Duration(2.0).sleep();
	gms_c.call(getmodelstate);
	now_y =  getmodelstate.response.pose.position.y;
      }

    ros::Duration(2.0).sleep();
    tw.linear.z = 0;
    tw.linear.x = 0;
    tw.linear.y = 0;
    publisher.publish(tw);

    
 

	
	action_.publishFeedback(feedback_);
	// this sleep is not necessary, the sequence is computed at 1    }
	
	if(success)
	  {
	    result_.result = feedback_.feedback;
	    ROS_INFO("%s: Succeeded", action_name_.c_str());
	    // set the action state to succeeded
	    action_.setSucceeded(result_);
	  }}
};




int main(int argc, char** argv)
{
  ros::init(argc, argv, "follower");

  cmdVel twister(ros::this_node::getName());
  ros::spin();

  return 0;
}
