# SPDX-FileCopyrightText: 2025 Keitaro Takeda
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    random = launch_ros.actions.Node(
            package='mypkg',
            executable='random',
            )
    checkcount = launch_ros.actions.Node(
            package='mypkg',
            executable='checkcount',
            output='screen'
            )
    return launch.LaunchDescription([random, checkcount])
