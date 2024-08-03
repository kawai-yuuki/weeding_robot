#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Bool
from roboflowoak import RoboflowOak

class CameraDetectionNode(Node):
    def __init__(self):
        super().__init__("camera_detection")
        self.detection_result = False
        self.rf = RoboflowOak(model="weeds-tuhor", confidence=0.05, overlap=0.5, 
                              version="1", api_key="", rgb=True, 
                              depth=False, device=None, blocking=True)
        self.presense_of_weeds_publisher_ = self.create_publisher(
            Bool, "presense_of_weeds", 10)
        self.publish_timer_ = self.create_timer(
            1.0, self.publish_presense_of_weeds)
        self.get_logger().info("Camera detection has been started.")

    def publish_presense_of_weeds(self):
        result, frame, raw_frame, depth = self.rf.detect()
        predictions = result["predictions"]
        if [p.json()['class'] for p in predictions]!=[]:
            self.detection_result = 'Weeds' in [p.json()['class'] for p in predictions]
        msg = Bool()
        msg.data = self.detection_result
        self.presense_of_weeds_publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CameraDetectionNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
