#!/usr/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Keitaro Takeda
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

ng() {
    echo "${1}行目が違うよ"
    res=1
}
res=0
cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 5 ros2 launch mypkg random_count.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |

if grep '以上';then
  echo Ok
else
  ng "$LINENO"
fi


cat /tmp/mypkg.log |

if grep '回目';then
  echo Ok
else
  ng "$LINENO"
fi

[ "$res" = 0 ] && echo OK
exit $res
