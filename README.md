# Industrial-robotic-_-final-project

ROS Simulation in Gazebo on Melodic about Open Rover robot shows different ways to control it.

##1. Install from source

Get the code:
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/alexvl06-ux/Industrial-robotic-_-final-project.git

Build the packages:
cd ~/catkin_ws
catkin_make

Don't forget to use those commands before you try to launch anything on the terminal (you can add them in your .bashrc) :

source /opt/ros/melodic/setup.bash 
source ~/catkin_ws/devel/setup.bash

Open Rover in Gazebo
Developed and tested on ROS Melodic/Gazebo 9.

Previous steps:

1.	Find input’s list:
    ls dev/input
![WhatsApp Image 2021-01-24 at 12 42 18 AM](https://user-images.githubusercontent.com/77949713/105666442-3c59ce80-5ea7-11eb-92c7-e0b0bb3317c7.jpeg)

2.	You will be able to see JS2 input in it. Now you have to set that input like a parameter in joy node:
    rosparam set joy_node/dev dev/input/js2 

3.	Execute joy_node of the joy package:
	    rosrun joy joy_node


Initializing GAZEBO

1.	Driving Open Rover robot in empty world: you will be able to drive the robot with the joystick and change its position directly. 
    Firstly, start Gazebo (empty world) and Open Rover model:
		    roslaunch rr_open_rover_simulation 2wd_rover_gazebo.launch

    finally, in a new terminal, execute the following command
		    rosrun rr_openrover_driver control_rover
		    ![WhatsApp Image 2021-01-24 at 12 42 46 AM](https://user-images.githubusercontent.com/77949713/105666682-cf930400-5ea7-11eb-9df1-24e4d89135a7.jpeg)


2.	Moving the robot through a place with obstacles, using two modes: autonomous and manual. The robot will be able to detect obstacles and change route in autounous mode.
    Firstly, start Gazebo (with a place model) and Open Rover model:
		    roslaunch rr_open_rover_simulation 2wd_rover_gazebo2_.launch

    Finally, in a new terminal, execute the following command:
		    rosrun rr_open_rover_driver control_rover2
		    ![WhatsApp Image 2021-01-24 at 12 43 24 AM](https://user-images.githubusercontent.com/77949713/105666907-4fb96980-5ea8-11eb-813f-e0e7dd852cd8.jpeg)

note: You must press triangle key in the joystick if you want to change mode.
