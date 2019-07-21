Ouster OS1 Lidar
****************
Specs
=====
*All below specs are for the OS1-16 lidar that was used in this project*
- Works on channels 16, 64, 128.
- Maximum range of 120 meters.
- Field of view of 33.2 degree vertically and 360 degree horizontally.
- Sampling rate of 327,680 points/second.

Setup lidar
===========
1. Connect lidar interface box to router that supports Gigabit connection.
2. Connect lidar to lidar interface box via cable.
3. Determine the ip address your router gave the lidar when it connected to the network and jot it down.
4. Determine your linux ip adress by running *ifconfig* in terminal and jot it down.
   
Ouster Github
=============
The following `Github page <https://github.com/ouster-lidar/ouster_example>`_ provides information on how to view raw data streams, visualize data and use a robot operating system (ROS) to save recorded data in a .bag file.
ROS commands can also replay data in .bag files and convert .bag files to .csv files.

.. note:: Some version of Linux running Ubuntu must be used. It is recommended to run Ubuntu 18.04 for best results. Follow instructions in *Ubuntu* page for more details on installing Linux with Ubuntu.

Variable reference
------------------
**<os1_hostname>** is the hostname/ip address of OS1-16 lidar.

**<udp_data_dest_ip>** is the destination ip address the lidar sends data

**<frame_size>** is the size of the visualization frame and can ONLY be the following: 512x10, 512x20, 1024x10, 1024x20, 2048x10.

Ouster client
-------------
The Ouster client allows users to see the raw data stream that the lidar is collecting and sending to the specified ip address.
Instruction on building the client in Linux can be found here `Building client <https://github.com/ouster-lidar/ouster_example/tree/master/ouster_client>`_.

Running client
++++++++++++++
1. cd /path/to/ouster_client_example
2. type *./ouster_client_example <os1_hostname> <udp_dest_ip>*

Ouster visualization
--------------------
The Ouster visualization is used for building a basic visualizer frame of collected lidar data. Instructions on building visualizer and it's dependencies can be found here `Building visualizer <https://github.com/ouster-lidar/ouster_example/tree/master/ouster_viz>`_.
The visualizer can be run in real time or with recorded data.

Running visualizer
++++++++++++++++++
1. cd /path/to/ouster_viz/build
2. *./viz -m <frame_size> <os1_hostname> <udp_data_dest_ip>*
 
Ouster ROS
----------
.. note:: For Ubuntu 18.04 users it is best to use **ROS Melodic** as **ROS Kinetic** (The ROS provided on the GitHub page) is only compatible with Ubuntu 16.04 and lower. 

Building the ROS Node can be found here `Building ROS Kinetic <https://github.com/ouster-lidar/ouster_example/tree/master/ouster_ros>`_.

For Ubuntu 16.04 users and lower: `Installation of ROS Kinetic <http://wiki.ros.org/kinetic/Installation/Ubuntu>`_

For Ubuntu 18.04 users: `Installation of ROS Melodic <http://wiki.ros.org/melodic/Installation/Ubuntu>`_

For new users to using ROS: `ROS Tutorials <http://wiki.ros.org/ROS/Tutorials>`_

Running ROS Node
++++++++++++++++

.. note:: Before typing any commands make sure to always source the setup.bash file in your created ROS workspace otherwise it will return a error. The file can be sourced with the command *source /path/to/myworkspace/devel/setup.bash*.

For recording lidar data:

1. *roslaunch ouster_ros os1.launch os1_hostname:=<os1_hostname> os1_udp_dest:=<os1_udp_dest> lidar_mode<:=<lidar_mode>*. The option to visualize live data can be turned on by adding *viz:=true* to the roslaunch command.

2. *rosbag record -O <recorded__bag_filename> /os1_node/imu_packets /os1_node/lidar_packets* in a new terminal

*/os1_node/imu_packets* and */os1_node/lidar_packets* are your topic names that the lidar sends messages to via the node you built. These topic names can be changed to user preference.

.. note:: DO NOT close the terminal with the roslaunch command open otherwise rosbag will crash.

For replaying lidar data:

1. *roslaunch ouster_ros os1.launch replay:=true os1_hostname:=<os1_hostname>*
2. In a **new** terminal run *rosbag play <bag_filename>*

.. note:: DO NOT close the terminal with the roslaunch command open otherwise rosbag will crash.

Converting data to csv file: Run *rostopic echo "topic name" -b "bag_filename" -p > filename.csv*

.. note:: To find topic names run the command *rosbag info <bag_filename>*
