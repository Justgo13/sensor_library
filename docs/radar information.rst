Radar Information
*****************
Novelda X4
==========
The X4 radars are IR-UWB and can work at frequencies ranging from 6 GHz to 10.2 GHz. The total number of bins that can be sampled is 1536.

Specifications
--------------
X4M300 Specs
++++++++++++
- Detection Time: 1.5 - 3.0 seconds
- Range: 9.4 meters
- Antenna: Tx for transmission and Rx for receiving
- Baseband data output: 17 baseband/ssecond
- System on chip: Novelda UWB X4

X4M200 Specs
++++++++++++
- Detection Time: 3.0  - 5.0 seconds
- Range: 5 meters
- Antenna: Tx for transmission and Rx for receiving
- Baseband data output: 17 baseband/ssecond
- System on chip: Novelda UWB X4

Configuring X4 radar
--------------------
1. Begin by initializing to default values using prebuilt function *x4driver_init()*
2. Set PRF using function *x4driver_set_prf_div(...)*
   
.. note:: The common PLL value of 243 MHz is divided by the arguemnent passed in to *x4driver_set_prf_div(...)* to get a PRF value

.. note:: Make sure that when changing the PRF that frame length is shorter than 1/PRF and avoid sampling previous pulse when transmitting next pulse.

3. Set DAC sweep range minimum and maximum using *x4driver_set_dac_min()* and *x4driver_set_dac_max()*
4. Set 0 reference using *x4driver_set_frame_area_offset()*
5. Set frame area using function *x4driver_set_frame_area()* that takes two arguements, one for start of frame and one for end of frame.

Setting radar FPS
-----------------
To set the radar FPS the following parameters are required, PRF, iterations, pulse per step, dac max and dac min range as well as duty cycle.

.. math::
   
    FPS = \frac{PRF}{iteration*pulse_per_step*(dac_max-dac_min+1)} * duty cycle

Our Novelda radar is configured to a FPS of 17 pulse/second so if you wanted to change FPS then the above parameter would need to be changed. 

.. note:: The resulting FPS can be read using the built-in function *x4driver_get_fps()*.

Example pulse_per_step calculation
++++++++++++++++++++++++++++++++++
- PRF: 16 MHz
- X4_duty_cycle: 95%
- dac_max: 1100
- dac_min: 949
- iteration: 64
- FPS: 17
 
.. math::
   
   pulse\_per\_step &= \frac{PRF}{iteration*FPS*(dac_max-dac_min+1} * D \\
   pulse\_per\_step  &= \frac{16 MHz}{64*17*150} * 0.95 \\
   pulse\_per\_step  &= 87 

TSW1400
=======
The TSW1400 board is used to interface with TI radars.

Specifications
--------------
- Operates using 5 V power source and is controlled by the SW7 switch.
- 11 LEDS used to indicate presence of power and state of FPGA.
- Control of the TSW1400 is via USB cable to a Windows PC.

Refer to :download:`TSW1400 Comprehensive Guide <TI_softwares/mmWave_sensor_raw_data_capture_using_TSW1400_board_v2.pdf>` for full guide on hardware and software installations

Required softwares
------------------
:download:`mmWaveSDK <TI_softwares/mmwave_sdk_02_00_00_04-Windows-x86-Install.exe>`

:download:`mmWaveDFP <TI_softwares/mmwave_dfp_01_00_00_01_win32.exe>`

:download:`High speed data converter <TI_softwares/HSDC Pro v4.50/High Speed Data Converter Pro - Installer v4.50.exe>`

:download:`MATLAB runtime engine <TI_softwares/MCR_R2015aSP1_win32_installer.exe>`

.. note:: If you don't have Code Composer Studio v7.1 or higher installed get:

:download:`XDS Emulation Software Package <TI_softwares/ti_emupack_setup_8.0.27.9_win_32.exe>`


