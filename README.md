# AOLE_ROS
Pilot project for Aalto University Factory of the Future in the Cloud

**Version 1.0.2**

## Dependencies

Operating System: Ubuntu 18.04;

Installed Robot Operationg System (ROS), version - melodic (installation instruction: http://wiki.ros.org/ROS/Installation);

Installed Gazebo simulator, version 9.0.0

## Running Simulation

**1. Open a terminal window and type the following command to initialize simulation and robot description nodes:**

roslaunch mir_gazebo mir_SF_world.launch 

**2. Open another terminal window and type the following command to initialize the position controller node:**

rosrun move_node old_contr.py 

The node takes coordinates and provides velocity control signals to the robot

**3. The control node code can be accessed at "/home/amr/catkin_ws_3/src/mir_robot/move_node/src/old_contr.py".**

Change the control algorithm according to your needs.

## Possible improvements

Different improvements can be made to optimize and develop the project in future:

1. Put ROS nodes-topics communication-related parts of **old_contr.py** script into separate file in order to receive a higher level of abstraction during development of control algorithm.

2. Include SLAM (Simultaneous Localization And Mapping) algorithm into control node by using LiDAR sensor data 

3. Add more models related to Aalto Smart Factory (e.g. Conveyors) to the environment world

4. Implement control of several robots

## Contributors

- Ivan Kolodko <ivan.kolodko@aalto.fi>
- Udayanto Atmojo <udayanto.atmojo@aalto.fi>
