                    
import rclpy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from rclpy.node import Node
from angles import normalize_angle
import math


class Stalker(Node):

    def __init__(self):
        super().__init__('stalker')
        self.sub_pose_1=self.create_subscription(Pose,"/turtle1/pose",self.send_pose_1,10)
        #self.sub_vel_2=self.create_subscription(Twist,"/turtle1/cmd_vel",self.send_vel_1,10)
        self.sub_pose_2=self.create_subscription(Pose,"/turtle2/pose",self.send_pose_2,10)
        self.pub=self.create_publisher(Twist,"/turtle2/cmd_vel",10)
        self.timer=self.create_timer(0.1,self.error_calculation)
        self.turtle_1_pose=Pose()
        self.turtle_2_vel=Twist()
        self.turtle_2_pose=Pose()
        self.get_logger().info("Stalker mode activated: Let's start stalking !")
        self.dx=0
        self.dy=0
        self.del_theta=0
        self.s=0
        
    def send_pose_1(self,pose: Pose):
        self.turtle_1_pose= pose
        pass

    def send_pose_2(self,pose: Pose):
        self.turtle_2_pose=pose
        pass
    
    def error_calculation(self):
        self.dx= self.turtle_1_pose.x - self.turtle_2_pose.x
        self.dy= self.turtle_1_pose.y - self.turtle_2_pose.y
        #self.del_theta=self.turtle_1_pose.theta-self.turtle_2_pose.theta
        self.del_theta= math.atan2(self.dy,self.dx)-self.turtle_2_pose.theta
        self.s=math.sqrt((self.dx)**2+(self.dy)**2)
        self.del_theta=normalize_angle(self.del_theta)
        #if self.del_theta>math.pi :
        #    self.del_theta= -(2*(math.pi)-self.del_theta)
        #    pass
        #if self.del_theta<(-(math.pi)):
        #    self.del_theta=self.del_theta+(2*(math.pi))

        if self.s> 0.01 :
            self.turtle_2_vel.linear.x=(self.s*1.2)
            self.turtle_2_vel.angular.z=(self.del_theta*2.0)
            self.pub.publish(self.turtle_2_vel)
            pass

        pass
    
    
'''
    def send_vel_1(self,twist:Twist):
        self.current_vel=twist
        pass
    
'''
               
'''
    def post_vel_2(self):
        
     self.pub.publish(self.current_vel)
    
     pass
'''

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
