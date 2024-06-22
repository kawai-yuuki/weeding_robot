// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interfaces:msg/FrontSensor.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__MSG__DETAIL__FRONT_SENSOR__BUILDER_HPP_
#define MY_ROBOT_INTERFACES__MSG__DETAIL__FRONT_SENSOR__BUILDER_HPP_

#include "my_robot_interfaces/msg/detail/front_sensor__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace my_robot_interfaces
{

namespace msg
{

namespace builder
{

class Init_FrontSensor_rear_sensor_data
{
public:
  explicit Init_FrontSensor_rear_sensor_data(::my_robot_interfaces::msg::FrontSensor & msg)
  : msg_(msg)
  {}
  ::my_robot_interfaces::msg::FrontSensor rear_sensor_data(::my_robot_interfaces::msg::FrontSensor::_rear_sensor_data_type arg)
  {
    msg_.rear_sensor_data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::msg::FrontSensor msg_;
};

class Init_FrontSensor_front_sensor_data
{
public:
  Init_FrontSensor_front_sensor_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FrontSensor_rear_sensor_data front_sensor_data(::my_robot_interfaces::msg::FrontSensor::_front_sensor_data_type arg)
  {
    msg_.front_sensor_data = std::move(arg);
    return Init_FrontSensor_rear_sensor_data(msg_);
  }

private:
  ::my_robot_interfaces::msg::FrontSensor msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::msg::FrontSensor>()
{
  return my_robot_interfaces::msg::builder::Init_FrontSensor_front_sensor_data();
}

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__MSG__DETAIL__FRONT_SENSOR__BUILDER_HPP_
