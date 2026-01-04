# SPDX-FileCopyrightText: 2025 Keitaro Takeda
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String


rclpy.init()
node = Node("listener")
c = {}
pub = node.create_publisher(String, "numcou", 10)

def cb(msg):
    n = int(msg.data)
    i = f'{n}以上{n+1}未満'

    if i not in c:
        c[i] = 0
    c[i] += 1

    node.get_logger().info(f'{i}（{c[i]}回目）')

    lines = []

    for k in sorted(c.keys()):
        lines.append(f'{k}: {c[k]}回')

    cou_msg = String()
    cou_msg.data = '\n'.join(lines)
    pub.publish(cou_msg)


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
