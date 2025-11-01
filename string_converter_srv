from tutorial_interfaces.srv import CapsLock                        
import rclpy
from std_msgs.msg import String
from rclpy.node import Node


class CustNode(Node):

    def __init__(self):
        super().__init__('cust_node')

        # service
        self.srv = self.create_service(CapsLock, 'caps_lock', self.send_callback)
        self.get_logger().info('Service ready.')
        self.switch = 1

        # client 
        self.cli = self.create_client(CapsLock, 'caps_lock')       
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        
        self.req = CapsLock.Request()  
                               
    # service callback fn
    def send_callback(self, request, response):
        input_str = request.input
        response.output = input_str.upper()
        self.get_logger().info(f"Converted: {input_str} => {response.output}")
        return response

    # client request fn (synchronous)
    def send_request(self):
        self.req.input = input("Enter string to be converted: ")
        if self.req.input == "X":
            self.switch = 0
            return None
   
       
        response = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self,response)
        return response.result()


def main():
    rclpy.init()
    node = CustNode()

    print("Enter X to exit.")
    
    while node.switch == 1:
        response = node.send_request()
        if node.switch == 0:
            print("Exiting...")
            break
        print("Converted:", response.output)
        print("Enter X to exit")

    rclpy.shutdown()


if __name__ == '__main__':
    main()
