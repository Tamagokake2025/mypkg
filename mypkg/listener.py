# SPDX-FileCopyrightText: 2025 Keitaro Takeda
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


rclpy.init()
node = Node("listener")

def cb(msg):
    global node
    n = int(msg.data)
    node.get_logger().info(f'{n}以上{n+1}以下' )


def main():
    pub = node.create_subscription(Float32, "rannum", cb, 10)
    rclpy.spin(node)
