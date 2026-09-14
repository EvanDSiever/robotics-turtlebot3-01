import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from std_msgs.msg import Float32

class SensorSubscriber(Node):
    def __init__(self):
        super().__init__('sensor_subscriber')
        self.declare_parameter('reliability', 'reliable')
        self.declare_parameter('depth', 10)

        rel = (ReliabilityPolicy.RELIABLE 
               if self.get_parameter('reliability').value == 'reliable' 
               else ReliabilityPolicy.BEST_EFFORT)

        qos = QoSProfile(
            depth=self.get_parameter('depth').value,
            reliability=rel,
            history=HistoryPolicy.KEEP_LAST
        )

        self.count = 0
        self.sub = self.create_subscription(
            Float32,
            'sensor_data',
            self.on_data,
            qos
        )
        self.get_logger().info(f'Subscriber ready, qos={rel.name}')

    def on_data(self, msg):
        self.count += 1
        self.get_logger().info(f'Received #{self.count}: {msg.data:.3f}')

def main():
    rclpy.init()
    node = SensorSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
