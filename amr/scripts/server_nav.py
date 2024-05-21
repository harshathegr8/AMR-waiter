#!/usr/bin/env python3
import rospy
from move_base_msgs.msg import MoveBaseActionGoal
from std_msgs.msg import String
import tf
from geometry_msgs.msg import Quaternion,PoseWithCovarianceStamped
from std_msgs.msg import String
from actionlib_msgs.msg import GoalStatusArray

def callback(data):
    pub = rospy.Publisher("move_base/goal",MoveBaseActionGoal,queue_size=0)
    a = data.data[:-1]
    if str(a)=="Order1":
    	table1 = MoveBaseActionGoal()
    	table1.goal.target_pose.header.stamp = rospy.rostime.Time.now()
    	table1.header.stamp = rospy.rostime.Time.now()
    	table1.goal.target_pose.header.frame_id = 'map' 
    	table1.goal.target_pose.pose.orientation.z = 0.665
    	table1.goal.target_pose.pose.orientation.w = 0.747
    	table1.goal.target_pose.pose.position.x = -3.145
    	table1.goal.target_pose.pose.position.y = 5.353
    	pub.publish(table1)
    elif str(a)=="Order2":
    	table1 = MoveBaseActionGoal()
    	table1.goal.target_pose.header.stamp = rospy.rostime.Time.now()
    	table1.header.stamp = rospy.rostime.Time.now()
    	table1.goal.target_pose.header.frame_id = 'map' 
    	table1.goal.target_pose.pose.orientation.z = -0.703
    	table1.goal.target_pose.pose.orientation.w = 0.711
    	table1.goal.target_pose.pose.position.x = -2.08
    	table1.goal.target_pose.pose.position.y = -1.226
    	pub.publish(table1)
    elif str(a)=="gotokitchen":
    	table1 = MoveBaseActionGoal()
    	table1.goal.target_pose.header.stamp = rospy.rostime.Time.now()
    	table1.header.stamp = rospy.rostime.Time.now()
    	table1.goal.target_pose.header.frame_id = 'map' 
    	table1.goal.target_pose.pose.orientation.z = 0.679
    	table1.goal.target_pose.pose.orientation.w = 0.734
    	table1.goal.target_pose.pose.position.x = -0.293
    	table1.goal.target_pose.pose.position.y = 6.072
    	pub.publish(table1) 
def listener():
    global processing, new_msg, msg
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('server_cmd', anonymous=True)
    rospy.Subscriber("command", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    
    rospy.spin()

if __name__ == '__main__':
    listener()
