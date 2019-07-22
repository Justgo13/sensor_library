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

Command to run: *python X4_record_playback.py -d com3-b -r*

- *-d com3* represents device name and can be found when starting Xethru Xplorer.
- *-b* to use baseband to record, default is radio frequency.
- *-r* to start recording.

The pymoduleconnector library is used as an import in the X4 record and playback code and can be downloaded with the link below:

`pymoduleconnector library download <https://www.xethru.com/community/threads/module-connector-raspberry-pi.136/>`_

.. automodule:: X4_record_playback
   :members:

X4 Threshold detection
======================
To use these functions first take the data recorded from the X4 radar and pass it into the iq_data() function found in X4_parser.py to get a comlex csv file. The file received will
be used wherever *filename* is an arguement.

.. automodule:: X4_threshold
   :members:
   
