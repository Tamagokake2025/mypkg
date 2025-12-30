# SPDX-FileCopyrightText: 2025 Keitaro Takeda
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


rclpy.init()
node = Node("listener")
c = {}

def cb(msg):
    n = int(msg.data)
    i = f'{n}以上{n+1}以下'

    if i not in c:
        c[i] = 0
    c[i] += 1

    node.get_logger().info(f'{i}（{c[i]}回目）')

def main():
    try:
        pub = node.create_subscription(Float32, "rannum", cb, 10)
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()



if __name__ == '__main__':
    main()
