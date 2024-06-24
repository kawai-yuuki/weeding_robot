from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    camera_detection_node = Node(
        package="weeding_robot",
        executable="camera_detection"
    )

    weeding_motor_node = Node(
        package="weeding_robot",
        executable="weeding_motor",
        parameters=[
            
        ]
    )

    sensor_node = Node(
        package="weeding_robot",
        executable="sensor",
        parameters=[
            {"publish_frequency": 2.0}
        ]
    )

    driving_motor_node = Node(
        package="weeding_robot",
        executable="driving_motor",
        parameters=[

        ]
    )

    ld.add_action(camera_detection_node)
    ld.add_action(weeding_motor_node)
    ld.add_action(sensor_node)
    ld.add_action(driving_motor_node)
    return ld