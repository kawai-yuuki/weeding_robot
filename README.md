# weeding_robot

![Image](image/weeding_robot.jpg)
![Image](https://github.com/kawai-yuuki/weeding_robot/blob/main/image/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202024-01-14%2019.51.26.png)

## Overview

This is the source code of the weeding robot I made for my senior year graduation project. When the robot detects a weed using an object detection model, it rotates a nylon cord cutter to cut the weed.

## Requirement

### Software
Ubuntu 20.04  
ROS2 Foxy  
roboflow  
pigpio  
etc...

### Hardware
Raspberry Pi 4B 4GB  
Luxionis OAK-D S2 (fixed focus)  
TAMIYA Educational Construction Series  
etc...

## Usage
```
sudo pigpiod
ros2 launch weeding_robot weeding_robot.launch.py
```
## Features

It moves along the wall using two distance sensors and automatically removes weeds that grow between the ground and the wall.If no weeds are detected, the nylon cord cutter stops, reducing wasted energy consumption and flying debris.

## Reference

https://www.udemy.com/course/ros2-for-beginners/?couponCode=ST18MT62524  
https://www.amazon.co.jp/dp/B0C6W3G5K7?psc=1&ref=ppx_yo2ov_dt_b_product_details

## Author

Yuki Kawai  
Tokyo Denki University  
IoE/M2M solution lab

## Licence

The source code is licensed MIT. The website content is licensed CC BY 4.0,see LICENSE.
