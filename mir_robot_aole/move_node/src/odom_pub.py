#!/usr/bin/env python

import rospy
from nav_msgs.msg import  Odometry
from std_msgs.msg import Header
from gazebo_msgs.srv import GetModelState, GetModelStateRequest



rospy.init_node('odom_pub')


odom_pub=rospy.Publisher('/my_odom',Odometry,queue_size=5)

rospy.wait_for_service('/gazebo/get_model_state')
get_model_srv = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)


odom = Odometry()
header = Header()
header.frame_id = '/odom'

model = GetModelStateRequest()
model.model_name = 'mir'

r = rospy.Rate(2) #how often odometry publihes

while not rospy.is_shotdown():

	result = get_model_srv(model)

	odom.pose.pose = result.pose
	odom.twist.twist = result.twist

	header.stamp = rospy.Time.now()
	odom.header = header

	odom_pub.publish(odom)

	r.sleep()


