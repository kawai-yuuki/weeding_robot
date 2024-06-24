from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    sensor_node = Node(
        package="weeding_robot",
        executable="sensor",
        parameters=[
            {"publish_frequency": 4.0}
        ]
    )

    driving_motor_node = Node(
        package="weeding_robot",
        executable="driving_motor",
        parameters=[

        ]
    )


    ld.add_action(sensor_node)
    ld.add_action(driving_motor_node)
    return ld