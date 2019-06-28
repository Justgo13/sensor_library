X4 Radar
********

Parser for iq data
==================
Pass your .dat file from the recording into this function to generate a readable csv file with complex values as data.
.. automodule:: X4_parser
   :members: iq_data

Parser for raw data
===================
Pass your .dat file from the recording into this function to generate a readable csv file with raw values as data.
.. automodule:: X4_parser
   :noindex:
   :members: raw_data


X4 Record and playback code
===========================
Target module: X4M200,X4M300,X4M03

Introduction:

XeThru modules support both RF and baseband data output. This is an example of radar raw data manipulation.
Developer can use Module Connecter API to read, record radar raw data, and also playback recorded data. 

Command to run: *python X4_record_playback.py -d com3-b -r*

- *-d com3* represents device name and can be found when starting Xethru Xplorer.
- *-b* to use baseband to record, default is radio frequency.
- *-r* to start recording.

.. automodule:: X4_record_playback
   :members: 
