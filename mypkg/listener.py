# SPDX-FileCopyrightText: 2025 Keitaro Takeda
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


rclpy.init()
node = Node("listener")

def cb(msg):
    global node
    node.get_logger().info("乱数: %f" %msg.data)


def main():
    pub = node.create_subscription(Float32, "rannum", cb, 10)
    rclpy.spin(node)
