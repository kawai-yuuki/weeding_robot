// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from my_robot_interfaces:msg/RearSensor.idl
// generated code does not contain a copyright notice
#include "my_robot_interfaces/msg/detail/rear_sensor__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
my_robot_interfaces__msg__RearSensor__init(my_robot_interfaces__msg__RearSensor * msg)
{
  if (!msg) {
    return false;
  }
  // rear_sensor_data
  return true;
}

void
my_robot_interfaces__msg__RearSensor__fini(my_robot_interfaces__msg__RearSensor * msg)
{
  if (!msg) {
    return;
  }
  // rear_sensor_data
}

bool
my_robot_interfaces__msg__RearSensor__are_equal(const my_robot_interfaces__msg__RearSensor * lhs, const my_robot_interfaces__msg__RearSensor * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // rear_sensor_data
  if (lhs->rear_sensor_data != rhs->rear_sensor_data) {
    return false;
  }
  return true;
}

bool
my_robot_interfaces__msg__RearSensor__copy(
  const my_robot_interfaces__msg__RearSensor * input,
  my_robot_interfaces__msg__RearSensor * output)
{
  if (!input || !output) {
    return false;
  }
  // rear_sensor_data
  output->rear_sensor_data = input->rear_sensor_data;
  return true;
}

my_robot_interfaces__msg__RearSensor *
my_robot_interfaces__msg__RearSensor__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_robot_interfaces__msg__RearSensor * msg = (my_robot_interfaces__msg__RearSensor *)allocator.allocate(sizeof(my_robot_interfaces__msg__RearSensor), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(my_robot_interfaces__msg__RearSensor));
  bool success = my_robot_interfaces__msg__RearSensor__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
my_robot_interfaces__msg__RearSensor__destroy(my_robot_interfaces__msg__RearSensor * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    my_robot_interfaces__msg__RearSensor__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
my_robot_interfaces__msg__RearSensor__Sequence__init(my_robot_interfaces__msg__RearSensor__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_robot_interfaces__msg__RearSensor * data = NULL;

  if (size) {
    data = (my_robot_interfaces__msg__RearSensor *)allocator.zero_allocate(size, sizeof(my_robot_interfaces__msg__RearSensor), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = my_robot_interfaces__msg__RearSensor__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        my_robot_interfaces__msg__RearSensor__fini(&data[i - 1]);
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
my_robot_interfaces__msg__RearSensor__Sequence__fini(my_robot_interfaces__msg__RearSensor__Sequence * array)
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
      my_robot_interfaces__msg__RearSensor__fini(&array->data[i]);
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

my_robot_interfaces__msg__RearSensor__Sequence *
my_robot_interfaces__msg__RearSensor__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_robot_interfaces__msg__RearSensor__Sequence * array = (my_robot_interfaces__msg__RearSensor__Sequence *)allocator.allocate(sizeof(my_robot_interfaces__msg__RearSensor__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = my_robot_interfaces__msg__RearSensor__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
my_robot_interfaces__msg__RearSensor__Sequence__destroy(my_robot_interfaces__msg__RearSensor__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    my_robot_interfaces__msg__RearSensor__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
my_robot_interfaces__msg__RearSensor__Sequence__are_equal(const my_robot_interfaces__msg__RearSensor__Sequence * lhs, const my_robot_interfaces__msg__RearSensor__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!my_robot_interfaces__msg__RearSensor__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
my_robot_interfaces__msg__RearSensor__Sequence__copy(
  const my_robot_interfaces__msg__RearSensor__Sequence * input,
  my_robot_interfaces__msg__RearSensor__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(my_robot_interfaces__msg__RearSensor);
    my_robot_interfaces__msg__RearSensor * data =
      (my_robot_interfaces__msg__RearSensor *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!my_robot_interfaces__msg__RearSensor__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          my_robot_interfaces__msg__RearSensor__fini(&data[i]);
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
    if (!my_robot_interfaces__msg__RearSensor__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
