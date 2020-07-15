#!/usr/bin/env python


# Import libraries

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import  Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point
from math import atan2,sqrt,pow,pi
import time

# Declaring robot state variables

x=0 # robot x coordinate
y=0 # robot y coordinate
theta=0 # robot yaw angle

msg=Odometry() # get messages from Odometry topic

def position(msg): # function updating robot current state
    global x
    global y
    global theta

    x=msg.pose.pose.position.x # current x coordinate
    y=msg.pose.pose.position.y # current y coordinate
    ora_q=msg.pose.pose.orientation # cuurent orientation described with quaternions
    (roll,pitch,theta)=euler_from_quaternion([ora_q.x,ora_q.y,ora_q.z,ora_q.w]) # calculation of eulers angles from quaternions

rospy.init_node('Position_Controller') # initializing the current node so it can be observed by ROS
sub=rospy.Subscriber('/odom_comb',Odometry,callback=position) # Subscribe the node to the /odom_comb topic to receive the odometry information
pub=rospy.Publisher('/cmd_vel',Twist,queue_size=10) # Publish messages to the /cmd_vel topic
rospy.sleep(1) # pause between messages
r=rospy.Rate(4) # message sending frequency [Hz]

#to set a goal

goal=Point() # goal is the same type as Point() messages

goal.x=int(raw_input("Insert X coordinate: ")) # provide UI for goal x coordinate

goal.y=int(raw_input("Insert Y coordinate: ")) # provide UI for goal y coordinate

speed=Twist() # speed is the same type as Twist() messages


# main program loop

while not rospy.is_shutdown():

# define difference between goal and current state
    x_diff=goal.x-x 
    y_diff=goal.y-y

    distance=sqrt(pow(y_diff,2)+pow(x_diff,2))

# yaw angle the robot needs to point to the goal direction

    angle_to_go=atan2(y_diff,x_diff)

# if the difference between desired and current angles is big: rotate until the difference is small enought (0.1)

    if abs(angle_to_go-theta)>0.1:
        print('\x1b[6;30;42m' + 'Looking for the right angle' + '\x1b[0m')
        speed.linear.x =0
        speed.angular.z=0.7 if (angle_to_go-theta)>0 else -0.7
        print("X : {:0.2f}, Y : {:0.2f} , theta : {},Angle To Go : {}, Error : {} ").format(x, y,theta,angle_to_go,angle_to_go-theta)
        print ("Remaining Distance",distance)

# if the difference between desired and current angles is fine and the distance to it is big: move to the goal direction

    elif distance>0.1:
        print('\x1b[2;33;44m' + 'Moving to target' + '\x1b[0m')

        speed=Twist()
        speed.linear.x =.3
        speed.angular.z=0.0
        print("X : {:0.2f}, Y : {:0.2f} , theta : {},Angle To Go : {}, Error : {} ").format(x, y, theta, angle_to_go,angle_to_go-theta)

# if the distance is shorter than 0.1m: the goal is reached

    elif distance <= 0.1:
        print('\x1b[4;30;41m' + "--------------Goal reached--------------" + '\x1b[0m')
        t=Twist()
        pub.publish(t)
        print""
        print""
        t2 = time.time()

        print "Distance : ",distance
        print('\x1b[5;30;43m' + "--------------Enter New Coordinates--------------" + '\x1b[0m')

        goal.x = int(raw_input("Insert X coordinate: "))

        goal.y = int(raw_input("Insert Y coordinate: "))

    pub.publish(speed)
    r.sleep() 
