// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from my_robot_interfaces:msg/Sensor.idl
// generated code does not contain a copyright notice
#include "my_robot_interfaces/msg/detail/sensor__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
my_robot_interfaces__msg__Sensor__init(my_robot_interfaces__msg__Sensor * msg)
{
  if (!msg) {
    return false;
  }
  // front_sensor_data
  // rear_sensor_data
  return true;
}

void
my_robot_interfaces__msg__Sensor__fini(my_robot_interfaces__msg__Sensor * msg)
{
  if (!msg) {
    return;
  }
  // front_sensor_data
  // rear_sensor_data
}

bool
my_robot_interfaces__msg__Sensor__are_equal(const my_robot_interfaces__msg__Sensor * lhs, const my_robot_interfaces__msg__Sensor * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // front_sensor_data
  if (lhs->front_sensor_data != rhs->front_sensor_data) {
    return false;
  }
  // rear_sensor_data
  if (lhs->rear_sensor_data != rhs->rear_sensor_data) {
    return false;
  }
  return true;
}

bool
my_robot_interfaces__msg__Sensor__copy(
  const my_robot_interfaces__msg__Sensor * input,
  my_robot_interfaces__msg__Sensor * output)
{
  if (!input || !output) {
    return false;
  }
  // front_sensor_data
  output->front_sensor_data = input->front_sensor_data;
  // rear_sensor_data
  output->rear_sensor_data = input->rear_sensor_data;
  return true;
}

my_robot_interfaces__msg__Sensor *
my_robot_interfaces__msg__Sensor__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_robot_interfaces__msg__Sensor * msg = (my_robot_interfaces__msg__Sensor *)allocator.allocate(sizeof(my_robot_interfaces__msg__Sensor), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(my_robot_interfaces__msg__Sensor));
  bool success = my_robot_interfaces__msg__Sensor__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
my_robot_interfaces__msg__Sensor__destroy(my_robot_interfaces__msg__Sensor * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    my_robot_interfaces__msg__Sensor__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
my_robot_interfaces__msg__Sensor__Sequence__init(my_robot_interfaces__msg__Sensor__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_robot_interfaces__msg__Sensor * data = NULL;

  if (size) {
    data = (my_robot_interfaces__msg__Sensor *)allocator.zero_allocate(size, sizeof(my_robot_interfaces__msg__Sensor), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = my_robot_interfaces__msg__Sensor__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        my_robot_interfaces__msg__Sensor__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
my_robot_interfaces__msg__Sensor__Sequence__fini(my_robot_interfaces__msg__Sensor__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      my_robot_interfaces__msg__Sensor__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

my_robot_interfaces__msg__Sensor__Sequence *
my_robot_interfaces__msg__Sensor__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_robot_interfaces__msg__Sensor__Sequence * array = (my_robot_interfaces__msg__Sensor__Sequence *)allocator.allocate(sizeof(my_robot_interfaces__msg__Sensor__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = my_robot_interfaces__msg__Sensor__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
my_robot_interfaces__msg__Sensor__Sequence__destroy(my_robot_interfaces__msg__Sensor__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    my_robot_interfaces__msg__Sensor__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
my_robot_interfaces__msg__Sensor__Sequence__are_equal(const my_robot_interfaces__msg__Sensor__Sequence * lhs, const my_robot_interfaces__msg__Sensor__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!my_robot_interfaces__msg__Sensor__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
my_robot_interfaces__msg__Sensor__Sequence__copy(
  const my_robot_interfaces__msg__Sensor__Sequence * input,
  my_robot_interfaces__msg__Sensor__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(my_robot_interfaces__msg__Sensor);
    my_robot_interfaces__msg__Sensor * data =
      (my_robot_interfaces__msg__Sensor *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!my_robot_interfaces__msg__Sensor__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          my_robot_interfaces__msg__Sensor__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!my_robot_interfaces__msg__Sensor__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
