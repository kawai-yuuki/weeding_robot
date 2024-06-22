// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interfaces:msg/RearSensor.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__MSG__DETAIL__REAR_SENSOR__BUILDER_HPP_
#define MY_ROBOT_INTERFACES__MSG__DETAIL__REAR_SENSOR__BUILDER_HPP_

#include "my_robot_interfaces/msg/detail/rear_sensor__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace my_robot_interfaces
{

namespace msg
{

namespace builder
{

class Init_RearSensor_rear_sensor_data
{
public:
  Init_RearSensor_rear_sensor_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_robot_interfaces::msg::RearSensor rear_sensor_data(::my_robot_interfaces::msg::RearSensor::_rear_sensor_data_type arg)
  {
    msg_.rear_sensor_data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::msg::RearSensor msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::msg::RearSensor>()
{
  return my_robot_interfaces::msg::builder::Init_RearSensor_rear_sensor_data();
}

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__MSG__DETAIL__REAR_SENSOR__BUILDER_HPP_
