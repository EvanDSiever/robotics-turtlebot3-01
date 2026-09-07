FROM ros:humble-ros-base-jammy

# Build arguments matching your host account
ARG USERNAME=dev
ARG UID=1000
ARG GID=1000

# Install required build tools, visualization packages, and node demos
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash-completion \
    build-essential \
    git \
    python3-colcon-common-extensions \
    python3-pip \
    ros-humble-demo-nodes-cpp \
    ros-humble-demo-nodes-py \
    ros-humble-rqt-graph \
    ros-humble-rviz2 \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Create internal user matching host UID/GID
RUN groupadd --gid $GID $USERNAME \
    && useradd --uid $UID --gid $GID -m -s /bin/bash $USERNAME \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Set up primary workspace folder
RUN mkdir -p /ws/src && chown -R $USERNAME:$USERNAME /ws

# Copy and set entrypoint script permissions
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER $USERNAME
WORKDIR /ws

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]
