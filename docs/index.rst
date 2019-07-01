.. sensor_doc documentation master file, created by
   sphinx-quickstart on Sat Jun 15 13:29:56 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the CUDRDC project documentation!
********************************************

About project
=============
This project is funded by both the Defense Research and Development Canada (DRDC) and the National Research Council (NRC). These organizations are working alongside Carleton University students
to develop a pip installable library that contains all the parsers used to convert radar and lidar data to readable csv files. The library also contains methods for determining radar thresholds.
The radars used in this project are the Novelda X4M03, X4M300, X4M200 and the TSW1400. The lidar used is the Ouster OS1-16.

Contents:

.. toctree::
   :maxdepth: 2
   
   Radar information
   Linux setup
   X4 radar
   TI radar
   Ouster lidar
   Test

:download:`Novelda X4 binary file to complex or raw csv file<X4_parser.py>`

:download:`Novelda X4 data collection and playback<X4_record_playback.py>`

:download:`Novelda X4 threshold<X4_threshold.py>`

:download:`TI binary file to complex csv file<TI_parser.py>`

:download:`Unit tests for radar parser and Novelda threshold calculator<test.py>`

