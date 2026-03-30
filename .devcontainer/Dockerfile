# This Dockerfile installs xfce4, xvfb, x11vnc, novnc, and dbus-x11
FROM ubuntu:20.04

RUN apt-get update && \  
    apt-get install -y xfce4 xvfb x11vnc novnc dbus-x11 && \  
    apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
