                    
import rclpy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from rclpy.node import Node


class Stalker(Node):

    def __init__(self):
        super().__init__('stalker')
        self.sub1=self.create_subscription(Pose,"/turtle1/pose",self.send_vel_1,10)
        self.sub2=self.create_subscription(Twist,"/turtle1/cmd_vel",self.post_vel_1,10)
        #self.sub3=self.create_subscription(Pose,"/turtle2/pose")
        self.pub=self.create_publisher(Twist,"/turtle2/cmd_vel",10)
        self.current_pose=Pose()
        self.current_vel=Twist()
        self.turtle_2_pose=Pose()
        self.get_logger().info("Stalker mode activated: Let's start stalking !")
        
    def send_vel_1(self,pose: Pose):
        self.current_pose= pose
        
        

        pass

    def post_vel_1(self,twist:Twist):
        self.current_vel=twist
        self.pub.publish(self.current_vel)
        pass
    
    #def post_vel_2(self):
        
     # self.pub.publish(self.current_vel)
    
     # pass


def main():
    rclpy.init()
    stalker=Stalker()
    i=1
    for i in range (1,7):
        i+=i
        rclpy.spin_once(stalker)
    
    rclpy.spin(stalker)  
    rclpy.shutdown()


if __name__ == '__main__':
    main()