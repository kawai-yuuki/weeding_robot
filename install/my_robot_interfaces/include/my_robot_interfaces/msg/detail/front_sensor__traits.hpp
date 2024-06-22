// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_robot_interfaces:msg/FrontSensor.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__MSG__DETAIL__FRONT_SENSOR__TRAITS_HPP_
#define MY_ROBOT_INTERFACES__MSG__DETAIL__FRONT_SENSOR__TRAITS_HPP_

#include "my_robot_interfaces/msg/detail/front_sensor__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<my_robot_interfaces::msg::FrontSensor>()
{
  return "my_robot_interfaces::msg::FrontSensor";
}

template<>
inline const char * name<my_robot_interfaces::msg::FrontSensor>()
{
  return "my_robot_interfaces/msg/FrontSensor";
}

template<>
struct has_fixed_size<my_robot_interfaces::msg::FrontSensor>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_robot_interfaces::msg::FrontSensor>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_robot_interfaces::msg::FrontSensor>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MY_ROBOT_INTERFACES__MSG__DETAIL__FRONT_SENSOR__TRAITS_HPP_
