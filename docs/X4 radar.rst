X4 Radar
********

Parser for iq data
==================

.. automodule:: X4_parser
   :members: iq_data

Parser for raw data
===================

.. automodule:: X4_parser
   :noindex:
   :members: raw_data


X4 Record and playback code
===========================
Target module: X4M200,X4M300,X4M03

Introduction:

XeThru modules support both RF and baseband data output. This is an example of radar raw data manipulation.
Developer can use Module Connecter API to read, record radar raw data, and also playback recorded data. 

Command to run: *python X4_record_playback.py -d com4 -b -r*

- *-d com3* represents device name and can be found when starting Xethru Xplorer.
- *-b* to use baseband to record.
- *-r* to start recording.

.. automodule:: X4_record_playback
   :members: 
