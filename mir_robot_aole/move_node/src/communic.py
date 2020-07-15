#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

PI = 3.1415926535897





class movement :

    def __init__(self):
        rospy.init_node('move_robot_node', anonymous=False)			
        self.pub_move = rospy.Publisher("/cmd_vel",Twist,queue_size=10)
	
        self.move = Twist()

    	

    def publish_vel(self):
        self.pub_move.publish(self.move)

    def move_forward(self):        
        self.move.linear.x=10
        self.move.angular.z=0.0

    def move_backward(self):      
        self.move.linear.x=-10
        self.move.angular.z=0.0

    def rotate_left(self):      
        self.move.linear.x=0
        self.move.angular.z=10.0

    def rotate_right(self):      
        self.move.linear.x=0
        self.move.angular.z=-10.0

    def stop(self):        
        self.move.linear.x=0
        self.move.angular.z=0.0  


"""if __name__ == "__main__":"""
   

 
