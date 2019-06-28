.. sensor_doc documentation master file, created by
   sphinx-quickstart on Sat Jun 15 13:29:56 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the CUDRDC project documentation!
********************************************

About project
=============
This project is funded by both the Defense Research and Development Canada (DRDC) and the National Research Council (NRC). These organizations are working alongside Carleton University students
to develop a pip installable library that contains all the parsers used to convert radar and lidar data to readable csv files.
The radars used in this project are the Novelda X4M03, X4M300, X4M200 and the TI-AWR1642. The lidar used is the Ouster OS1-16.

Contents:

.. toctree::
   :maxdepth: 2
   
   Radar information
   Linux setup
   X4 radar
   TI radar
   Ouster lidar
   Test

:download:`Convert X4 binary .dat file to csv<X4_parser.py>`

:download:`X4 data collection code<X4_record_playback.py>`

:download:`Convert TI binary .bin file to csv<TI_parser.py>`

:download:`Unit tests for radar parser<test.py>`

