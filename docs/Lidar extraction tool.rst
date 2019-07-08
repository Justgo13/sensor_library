Lidar Extraction Tool
*********************
The lidar extraction tool is used to extract relevant data from the /os1_node/lidar_packets and /os1_node/imu_packets topics that were created when recording using the Ouster OS1-16 lidar.
From the lidar_packets topic, the tool can extract data such as global timestamps, lidar timestamps, range, number of signal photons, etc. From the imu_packets topic,  the tool can extract
data such as global timestamp, IMU timestamp, acceleration in xyz and angular velocity in the xyz plane. The tool uses a GUI interface so that navigating it is simple.

This GUI tool also calculate the xyz cartesian coordinates using lidar packet data and fit it to a lidar coordinate frame.

Functions
=========

Lidar packet functions
----------------------
The below functions are used to read certain data categories as mentioned above from a csv file to the user through the use of the GUI interface.

.. automodule:: lidar_extract
   :members:

IMU packet functions
--------------------
The below functions are used to read certain data categories as mentioned above from a csv file to the user through the use of the GUI interface.

.. automodule:: imu_extract
   :members:

XYZ Coordinate functions
------------------------
The below functions are used to calculate xyz cartesian points onto a lidar coordinate frame using data extracted from the lidar packets

.. automodule:: Lidar_coordinate_frame
   :members:

