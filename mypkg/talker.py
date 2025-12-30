# SPDX-FileCopyrightText: 2025 Keitaro Takeda
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Float32, "rannum", 10)


def cb():
    msg = Float32()
    msg.data = random.uniform(0.0,10.0)
    pub.publish(msg)
    node.get_logger().info("%.3f" % msg.data)

def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)
