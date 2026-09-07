#!/bin/bash
set -e

# 1. Source the base ROS 2 underlay
source /opt/ros/humble/setup.bash

# 2. Source the custom workspace overlay if it exists
if [ -f /ws/install/setup.bash ]; then
  source /ws/install/setup.bash
fi

# 3. Execute the container's primary process
exec "$@"
