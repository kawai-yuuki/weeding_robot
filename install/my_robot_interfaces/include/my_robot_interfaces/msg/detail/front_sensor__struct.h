// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_robot_interfaces:msg/FrontSensor.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__MSG__DETAIL__FRONT_SENSOR__STRUCT_H_
#define MY_ROBOT_INTERFACES__MSG__DETAIL__FRONT_SENSOR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/FrontSensor in the package my_robot_interfaces.
typedef struct my_robot_interfaces__msg__FrontSensor
{
  double front_sensor_data;
  double rear_sensor_data;
} my_robot_interfaces__msg__FrontSensor;

// Struct for a sequence of my_robot_interfaces__msg__FrontSensor.
typedef struct my_robot_interfaces__msg__FrontSensor__Sequence
{
  my_robot_interfaces__msg__FrontSensor * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__msg__FrontSensor__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_ROBOT_INTERFACES__MSG__DETAIL__FRONT_SENSOR__STRUCT_H_
