# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ubuntu/ros2_ws/src/my_cpp_pkg

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ubuntu/ros2_ws/build/my_cpp_pkg

# Include any dependencies generated for this target.
include CMakeFiles/smartphone.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/smartphone.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/smartphone.dir/flags.make

CMakeFiles/smartphone.dir/src/smartphone.cpp.o: CMakeFiles/smartphone.dir/flags.make
CMakeFiles/smartphone.dir/src/smartphone.cpp.o: /home/ubuntu/ros2_ws/src/my_cpp_pkg/src/smartphone.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/ros2_ws/build/my_cpp_pkg/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/smartphone.dir/src/smartphone.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/smartphone.dir/src/smartphone.cpp.o -c /home/ubuntu/ros2_ws/src/my_cpp_pkg/src/smartphone.cpp

CMakeFiles/smartphone.dir/src/smartphone.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/smartphone.dir/src/smartphone.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ubuntu/ros2_ws/src/my_cpp_pkg/src/smartphone.cpp > CMakeFiles/smartphone.dir/src/smartphone.cpp.i

CMakeFiles/smartphone.dir/src/smartphone.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/smartphone.dir/src/smartphone.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ubuntu/ros2_ws/src/my_cpp_pkg/src/smartphone.cpp -o CMakeFiles/smartphone.dir/src/smartphone.cpp.s

# Object files for target smartphone
smartphone_OBJECTS = \
"CMakeFiles/smartphone.dir/src/smartphone.cpp.o"

# External object files for target smartphone
smartphone_EXTERNAL_OBJECTS =

smartphone: CMakeFiles/smartphone.dir/src/smartphone.cpp.o
smartphone: CMakeFiles/smartphone.dir/build.make
smartphone: /home/ubuntu/ros2_foxy/install/rclcpp/lib/librclcpp.so
smartphone: /home/ubuntu/ros2_foxy/install/example_interfaces/lib/libexample_interfaces__rosidl_typesupport_introspection_c.so
smartphone: /home/ubuntu/ros2_foxy/install/example_interfaces/lib/libexample_interfaces__rosidl_typesupport_c.so
smartphone: /home/ubuntu/ros2_foxy/install/example_interfaces/lib/libexample_interfaces__rosidl_typesupport_introspection_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/example_interfaces/lib/libexample_interfaces__rosidl_typesupport_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/libstatistics_collector/lib/liblibstatistics_collector.so
smartphone: /home/ubuntu/ros2_foxy/install/libstatistics_collector/lib/liblibstatistics_collector_test_msgs__rosidl_typesupport_introspection_c.so
smartphone: /home/ubuntu/ros2_foxy/install/libstatistics_collector/lib/liblibstatistics_collector_test_msgs__rosidl_generator_c.so
smartphone: /home/ubuntu/ros2_foxy/install/libstatistics_collector/lib/liblibstatistics_collector_test_msgs__rosidl_typesupport_c.so
smartphone: /home/ubuntu/ros2_foxy/install/libstatistics_collector/lib/liblibstatistics_collector_test_msgs__rosidl_typesupport_introspection_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/libstatistics_collector/lib/liblibstatistics_collector_test_msgs__rosidl_typesupport_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/std_msgs/lib/libstd_msgs__rosidl_typesupport_introspection_c.so
smartphone: /home/ubuntu/ros2_foxy/install/std_msgs/lib/libstd_msgs__rosidl_generator_c.so
smartphone: /home/ubuntu/ros2_foxy/install/std_msgs/lib/libstd_msgs__rosidl_typesupport_c.so
smartphone: /home/ubuntu/ros2_foxy/install/std_msgs/lib/libstd_msgs__rosidl_typesupport_introspection_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/std_msgs/lib/libstd_msgs__rosidl_typesupport_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/rcl/lib/librcl.so
smartphone: /home/ubuntu/ros2_foxy/install/rcl_interfaces/lib/librcl_interfaces__rosidl_typesupport_introspection_c.so
smartphone: /home/ubuntu/ros2_foxy/install/rcl_interfaces/lib/librcl_interfaces__rosidl_generator_c.so
smartphone: /home/ubuntu/ros2_foxy/install/rcl_interfaces/lib/librcl_interfaces__rosidl_typesupport_c.so
smartphone: /home/ubuntu/ros2_foxy/install/rcl_interfaces/lib/librcl_interfaces__rosidl_typesupport_introspection_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/rcl_interfaces/lib/librcl_interfaces__rosidl_typesupport_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/rmw_implementation/lib/librmw_implementation.so
smartphone: /home/ubuntu/ros2_foxy/install/rmw/lib/librmw.so
smartphone: /home/ubuntu/ros2_foxy/install/rcl_logging_spdlog/lib/librcl_logging_spdlog.so
smartphone: /usr/lib/aarch64-linux-gnu/libspdlog.so.1.5.0
smartphone: /home/ubuntu/ros2_foxy/install/rcl_yaml_param_parser/lib/librcl_yaml_param_parser.so
smartphone: /home/ubuntu/ros2_foxy/install/libyaml_vendor/lib/libyaml.so
smartphone: /home/ubuntu/ros2_foxy/install/rosgraph_msgs/lib/librosgraph_msgs__rosidl_typesupport_introspection_c.so
smartphone: /home/ubuntu/ros2_foxy/install/rosgraph_msgs/lib/librosgraph_msgs__rosidl_generator_c.so
smartphone: /home/ubuntu/ros2_foxy/install/rosgraph_msgs/lib/librosgraph_msgs__rosidl_typesupport_c.so
smartphone: /home/ubuntu/ros2_foxy/install/rosgraph_msgs/lib/librosgraph_msgs__rosidl_typesupport_introspection_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/rosgraph_msgs/lib/librosgraph_msgs__rosidl_typesupport_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/statistics_msgs/lib/libstatistics_msgs__rosidl_typesupport_introspection_c.so
smartphone: /home/ubuntu/ros2_foxy/install/statistics_msgs/lib/libstatistics_msgs__rosidl_generator_c.so
smartphone: /home/ubuntu/ros2_foxy/install/statistics_msgs/lib/libstatistics_msgs__rosidl_typesupport_c.so
smartphone: /home/ubuntu/ros2_foxy/install/statistics_msgs/lib/libstatistics_msgs__rosidl_typesupport_introspection_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/statistics_msgs/lib/libstatistics_msgs__rosidl_typesupport_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/tracetools/lib/libtracetools.so
smartphone: /home/ubuntu/ros2_foxy/install/example_interfaces/lib/libexample_interfaces__rosidl_generator_c.so
smartphone: /home/ubuntu/ros2_foxy/install/action_msgs/lib/libaction_msgs__rosidl_typesupport_introspection_c.so
smartphone: /home/ubuntu/ros2_foxy/install/action_msgs/lib/libaction_msgs__rosidl_generator_c.so
smartphone: /home/ubuntu/ros2_foxy/install/action_msgs/lib/libaction_msgs__rosidl_typesupport_c.so
smartphone: /home/ubuntu/ros2_foxy/install/action_msgs/lib/libaction_msgs__rosidl_typesupport_introspection_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/action_msgs/lib/libaction_msgs__rosidl_typesupport_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/builtin_interfaces/lib/libbuiltin_interfaces__rosidl_typesupport_introspection_c.so
smartphone: /home/ubuntu/ros2_foxy/install/builtin_interfaces/lib/libbuiltin_interfaces__rosidl_generator_c.so
smartphone: /home/ubuntu/ros2_foxy/install/builtin_interfaces/lib/libbuiltin_interfaces__rosidl_typesupport_c.so
smartphone: /home/ubuntu/ros2_foxy/install/builtin_interfaces/lib/libbuiltin_interfaces__rosidl_typesupport_introspection_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/builtin_interfaces/lib/libbuiltin_interfaces__rosidl_typesupport_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/unique_identifier_msgs/lib/libunique_identifier_msgs__rosidl_typesupport_introspection_c.so
smartphone: /home/ubuntu/ros2_foxy/install/unique_identifier_msgs/lib/libunique_identifier_msgs__rosidl_generator_c.so
smartphone: /home/ubuntu/ros2_foxy/install/unique_identifier_msgs/lib/libunique_identifier_msgs__rosidl_typesupport_c.so
smartphone: /home/ubuntu/ros2_foxy/install/unique_identifier_msgs/lib/libunique_identifier_msgs__rosidl_typesupport_introspection_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/rosidl_typesupport_introspection_cpp/lib/librosidl_typesupport_introspection_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/rosidl_typesupport_introspection_c/lib/librosidl_typesupport_introspection_c.so
smartphone: /home/ubuntu/ros2_foxy/install/unique_identifier_msgs/lib/libunique_identifier_msgs__rosidl_typesupport_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/rosidl_typesupport_cpp/lib/librosidl_typesupport_cpp.so
smartphone: /home/ubuntu/ros2_foxy/install/rosidl_typesupport_c/lib/librosidl_typesupport_c.so
smartphone: /home/ubuntu/ros2_foxy/install/rcpputils/lib/librcpputils.so
smartphone: /home/ubuntu/ros2_foxy/install/rosidl_runtime_c/lib/librosidl_runtime_c.so
smartphone: /home/ubuntu/ros2_foxy/install/rcutils/lib/librcutils.so
smartphone: CMakeFiles/smartphone.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ubuntu/ros2_ws/build/my_cpp_pkg/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable smartphone"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/smartphone.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/smartphone.dir/build: smartphone

.PHONY : CMakeFiles/smartphone.dir/build

CMakeFiles/smartphone.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/smartphone.dir/cmake_clean.cmake
.PHONY : CMakeFiles/smartphone.dir/clean

CMakeFiles/smartphone.dir/depend:
	cd /home/ubuntu/ros2_ws/build/my_cpp_pkg && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/ros2_ws/src/my_cpp_pkg /home/ubuntu/ros2_ws/src/my_cpp_pkg /home/ubuntu/ros2_ws/build/my_cpp_pkg /home/ubuntu/ros2_ws/build/my_cpp_pkg /home/ubuntu/ros2_ws/build/my_cpp_pkg/CMakeFiles/smartphone.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/smartphone.dir/depend

