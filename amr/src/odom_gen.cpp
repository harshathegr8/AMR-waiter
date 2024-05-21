#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "geometry_msgs/PoseWithCovarianceStamped.h"
#include "nav_msgs/Odometry.h"
float lin=10,ang=5;
long double cov[36] = {0.1,  0.0 , 0.0 , 0.0 , 0.0 , 0.0,
 0.0 , 0.1 , 0.0 , 0.0 , 0.0 , 0.0,
 0.0 ,  0.0 , 0.1 , 0.0 , 0.0 , 0.0,
 0.0 ,  0.0 , 0.0 , 0.1 , 0.0 , 0.0,
 0.0 ,  0.0 , 0.0 , 0.0 , 0.1 , 0.0,
 0.0 ,  0.0 , 0.0 , 0.0 , 0.0 , 0.1},x=0,y=0,z=0,ox=0,oy=0,oz=0,ow=0;

void callback(const geometry_msgs::Twist &cmd)
{
    lin = cmd.linear.x;ang = cmd.angular.z;   
}
void callback2(const geometry_msgs::PoseWithCovarianceStamped &amcl)
{
     x = amcl.pose.pose.position.x;
     y = amcl.pose.pose.position.y;
     z = amcl.pose.pose.position.z;
     ox = amcl.pose.pose.orientation.x;
     oy = amcl.pose.pose.orientation.y;
     oz = amcl.pose.pose.orientation.z;
     ow = amcl.pose.pose.orientation.w;int i;
     for(i=0;i<36;i++)
     {
     	cov[i] = amcl.pose.covariance[i];
     }
}

int main(int argc,char **agrv)
{
    ros::init(argc, agrv, "odom");
    ros::NodeHandle n;
    nav_msgs::Odometry odom_msg;
    ros::Publisher pub = n.advertise<nav_msgs::Odometry>("odom2", 0);
    ros::Subscriber sub = n.subscribe("cmd_vel", 0, callback);
    ros::Subscriber sub2 = n.subscribe("amcl_pose",0,callback2);
    ros::Rate loop_rate(10);
    while(ros::ok())
    {
        lin = 0;ang = 0;int i; 
        
    	ros::spinOnce();
    	for(i=0;i<36;i++)
     	{
     	    odom_msg.pose.covariance[i] = cov[i];
     	}
    	odom_msg.pose.pose.position.x = x;
    	odom_msg.pose.pose.position.y = y;
    	odom_msg.pose.pose.position.z = z;
    	odom_msg.pose.pose.orientation.x = ox;
    	odom_msg.pose.pose.orientation.y = oy;
    	odom_msg.pose.pose.orientation.z = oz;
    	odom_msg.pose.pose.orientation.w = ow;
    	odom_msg.twist.twist.linear.x = lin;
    	odom_msg.twist.twist.angular.z = ang;
    	
    	pub.publish(odom_msg);
    	loop_rate.sleep();
    }
    return 0;
}
