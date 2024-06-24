#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial
from example_interfaces.srv import SetBool
from roboflowoak import RoboflowOak

class DetectionClientNode(Node):
    def __init__(self):
        super().__init__("detection_client")
        self.rf = RoboflowOak(model="weeds-tuhor", confidence=0.05, overlap=0.5, 
                              version="1", api_key="SgN7kxjAfZ7qKQsNvFud", rgb=True, 
                              depth=False, device=None, blocking=True)
        

    def call_detection_server(self, data):
        client = self.create_client(SetBool, "detection")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server...")

        result, frame, raw_frame, depth = self.rf.detect()
        predictions = result["predictions"]

        if [p.json()['class'] for p in predictions]!=[]:
            print([p.json()['class'] for p in predictions][0])
            result = 'Weeds' in [p.json()['class'] for p in predictions]
        
        request = SetBool.Request()
        request.data = result

        future = client.call_async(request)
        future.detection_done_callback(
            partial(self.callback_call_detection, data))

    def callback_call_detection(self, future, data):
        try:
            response = future.result()
            self.get_logger().info(str(response.success))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))


def main(args=None):
    rclpy.init(args=args)
    node = DetectionClientNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
