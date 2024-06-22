// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_robot_interfaces:msg/RearSensor.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__MSG__DETAIL__REAR_SENSOR__STRUCT_HPP_
#define MY_ROBOT_INTERFACES__MSG__DETAIL__REAR_SENSOR__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__my_robot_interfaces__msg__RearSensor __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_interfaces__msg__RearSensor __declspec(deprecated)
#endif

namespace my_robot_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RearSensor_
{
  using Type = RearSensor_<ContainerAllocator>;

  explicit RearSensor_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->rear_sensor_data = 0.0;
    }
  }

  explicit RearSensor_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->rear_sensor_data = 0.0;
    }
  }

  // field types and members
  using _rear_sensor_data_type =
    double;
  _rear_sensor_data_type rear_sensor_data;

  // setters for named parameter idiom
  Type & set__rear_sensor_data(
    const double & _arg)
  {
    this->rear_sensor_data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_robot_interfaces::msg::RearSensor_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_interfaces::msg::RearSensor_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_interfaces::msg::RearSensor_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_interfaces::msg::RearSensor_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::msg::RearSensor_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::msg::RearSensor_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::msg::RearSensor_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::msg::RearSensor_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_interfaces::msg::RearSensor_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_interfaces::msg::RearSensor_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_interfaces__msg__RearSensor
    std::shared_ptr<my_robot_interfaces::msg::RearSensor_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_interfaces__msg__RearSensor
    std::shared_ptr<my_robot_interfaces::msg::RearSensor_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RearSensor_ & other) const
  {
    if (this->rear_sensor_data != other.rear_sensor_data) {
      return false;
    }
    return true;
  }
  bool operator!=(const RearSensor_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RearSensor_

// alias to use template instance with default allocator
using RearSensor =
  my_robot_interfaces::msg::RearSensor_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__MSG__DETAIL__REAR_SENSOR__STRUCT_HPP_
