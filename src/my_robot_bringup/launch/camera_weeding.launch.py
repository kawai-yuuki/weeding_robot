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


    ld.add_action(camera_detection_node)
    ld.add_action(weeding_motor_node)
    return ld