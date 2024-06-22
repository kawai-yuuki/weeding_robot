// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_robot_interfaces:msg/Sensor.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__MSG__DETAIL__SENSOR__STRUCT_HPP_
#define MY_ROBOT_INTERFACES__MSG__DETAIL__SENSOR__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__my_robot_interfaces__msg__Sensor __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_interfaces__msg__Sensor __declspec(deprecated)
#endif

namespace my_robot_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Sensor_
{
  using Type = Sensor_<ContainerAllocator>;

  explicit Sensor_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->front_sensor_data = 0.0;
      this->rear_sensor_data = 0.0;
    }
  }

  explicit Sensor_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->front_sensor_data = 0.0;
      this->rear_sensor_data = 0.0;
    }
  }

  // field types and members
  using _front_sensor_data_type =
    double;
  _front_sensor_data_type front_sensor_data;
  using _rear_sensor_data_type =
    double;
  _rear_sensor_data_type rear_sensor_data;

  // setters for named parameter idiom
  Type & set__front_sensor_data(
    const double & _arg)
  {
    this->front_sensor_data = _arg;
    return *this;
  }
  Type & set__rear_sensor_data(
    const double & _arg)
  {
    this->rear_sensor_data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_robot_interfaces::msg::Sensor_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_interfaces::msg::Sensor_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_interfaces::msg::Sensor_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_interfaces::msg::Sensor_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::msg::Sensor_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::msg::Sensor_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::msg::Sensor_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::msg::Sensor_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_interfaces::msg::Sensor_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_interfaces::msg::Sensor_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_interfaces__msg__Sensor
    std::shared_ptr<my_robot_interfaces::msg::Sensor_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_interfaces__msg__Sensor
    std::shared_ptr<my_robot_interfaces::msg::Sensor_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Sensor_ & other) const
  {
    if (this->front_sensor_data != other.front_sensor_data) {
      return false;
    }
    if (this->rear_sensor_data != other.rear_sensor_data) {
      return false;
    }
    return true;
  }
  bool operator!=(const Sensor_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Sensor_

// alias to use template instance with default allocator
using Sensor =
  my_robot_interfaces::msg::Sensor_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__MSG__DETAIL__SENSOR__STRUCT_HPP_
