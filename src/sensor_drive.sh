#!/bin/bash
export ROS_DOMAIN_ID=0
source /home/ubuntu/ros2_foxy/install/setup.bash
source /home/ubuntu/ros2_ws/install/setup.bash

ros2 launch my_robot_bringup sensor_drive.launch.py
