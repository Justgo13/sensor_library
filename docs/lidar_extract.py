import pandas

file = 'lidar_data3.csv'  # Recording csv file name
data = pandas.read_csv(file)  # Create pandas dataframe


def get_azimuth_block(azimuth_block_num):
    """
    Takes in a azimuth block number from 0-15 and returns the column in the csv file that the specified azimuth block
    starts at. This number will be useful when calling range, noise/signal photon and reflectivity.

    Example:

        >>> get_azimuth_block(0)
        >>> 1
    """
    if azimuth_block_num > 15 or azimuth_block_num < 0:
        print('Not a valid azimuth block number, please enter a number between 0-15')
        azimuth_block_num = int(input("Enter an azimuth block number to find it's starting column (0-15): "))
        get_azimuth_block(azimuth_block_num)

    return azimuth_block_num * 788 + 1


def get_timestamp(*args, single_row=False, multiple_row=False, row_section=False):
    """
    Takes in row arguements and boolean values and returns the lidar timestamp for those row(s).

    Parameters:

        single_row: boolean
            If this is set to true, output the timestamps for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the timestamps for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the timestamps for the row sections the user selected.

    Example:

        >>> get_timestamp[0,single_row=True]
        >>> [33.0202114185206, 33.0202116496, 33.0202117174244, 33.0202119463, 33.0202120189236, 33.020212246132, 33.0202123185122, 33.02021254748, 33.0202126186208, 33.020212861196, 33.020212917536, 33.02021314678, 33.020213218632, 33.02021345714, 33.020213518654, 33.020213754204]

    Returns:
    
        An array of all the timestamps the user desired to read.
    """
    timestamp = []
    arg = [*args]

    print("NOTE: All timestamps measured in seconds and each element is a timestamp for single azimuth block")
    if single_row is True:
        for col in range(1, len(data.columns)-1, 788):
            timestamp_segment = list(data.values[arg[0], col:col+8])
            timestamp_segment.reverse()
            timestamp_segment = [int(elem) for index, elem in enumerate(timestamp_segment)]
            del timestamp_segment[0:3]
            timestamp_segment[0] = float(timestamp_segment[0])
            time = float("".join(map(str, timestamp_segment)))
            timestamp.append(time)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            timestamp.append("new row")
            for col in range(1, len(data.columns)-1, 788):
                timestamp_segment = list(data.values[elem, col:col+8])
                timestamp_segment.reverse()
                timestamp_segment = [int(elem) for index, elem in enumerate(timestamp_segment)]
                del timestamp_segment[0:3]
                timestamp_segment[0] = float(timestamp_segment[0])
                time = float("".join(map(str, timestamp_segment)))
                timestamp.append(time)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            timestamp.append("new row")
            for col in range(1, len(data.columns)-1, 788):
                timestamp_segment = list(data.values[row, col:col+8])
                timestamp_segment.reverse()
                timestamp_segment = [int(elem) for index, elem in enumerate(timestamp_segment)]
                del timestamp_segment[0:3]
                timestamp_segment[0] = float(timestamp_segment[0])
                time = float("".join(map(str, timestamp_segment)))
                timestamp.append(time)

    return timestamp


def get_frame_id(*args, single_row=False, multiple_row=False, row_section=False):
    """
    Takes in row arguements and boolean values and returns the frame ID for those row(s).

    Parameters:

        single_row: boolean
            If this is set to true, output the frame IDs for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the frame IDs for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the frame IDs for the row sections the user selected.

    Example:

        >>> get_frame_id(0,single_row=True)
        >>> [222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237]

    Return:
    
        An array of all the frame IDs the user desired to read. 
    """
    frame_id = []
    arg = [*args]

    print("NOTE: Each element is a frame ID for single azimuth block")
    if single_row is True:
        for col in range(9, len(data.columns)-1, 788):
            frame_id_segment = list(data.values[arg[0], col:col+2])
            frame_id_segment.reverse()
            frame_id_segment = [int(elem) for index, elem in enumerate(frame_id_segment)]
            frame = int("".join(map(str, frame_id_segment)))
            frame_id.append(frame)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            frame_id.append("new row")
            for col in range(9,len(data.columns)-1, 788):
                frame_id_segment = list(data.values[elem, col:col+2])
                frame_id_segment.reverse()
                frame_id_segment = [int(elem) for index, elem in enumerate(frame_id_segment)]
                frame = int("".join(map(str, frame_id_segment)))
                frame_id.append(frame)
    elif row_section is True:
        for row in range(arg[0],arg[1]+1):
            frame_id.append("new row")
            for col in range(9, len(data.columns)-1, 788):
                frame_id_segment = list(data.values[row, col:col+2])
                frame_id_segment.reverse()
                frame_id_segment = [int(elem) for index, elem in enumerate(frame_id_segment)]
                frame = int("".join(map(str, frame_id_segment)))
                frame_id.append(frame)
                
    return frame_id


def get_measurement_id(*args, single_row=False, multiple_row=False, row_section=False):
    """
    Takes in row arguements and boolean values and returns the measurement ID for those row(s).

    Parameters:

        single_row: boolean
            If this is set to true, output the measurement IDs for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the measurement IDs for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the measurement IDs for the row sections the user selected.

    Example:

        >>> get_measurement_id(0,single_row=True)
        >>> [4239, 4239, 4239, 4239, 4239, 4239, 4239, 4239, 4239, 4239, 4239, 4239, 4239, 4239, 4239, 4239]

    Return:
    
        An array of all the measurement IDs the user desired to read.
    """
    measurement_id = []
    arg = [*args]

    print("NOTE: Each element is a measurement ID for single azimuth block")
    if single_row is True:
        for col in range(11, len(data.columns)-1,788):
            measurement_id_segment = list(data.values[arg[0], col:col+2])
            measurement_id_segment.reverse()
            measurement_id_segment = [int(elem) for index, elem in enumerate(measurement_id_segment)]
            measurement = int("".join(map(str, measurement_id_segment)))
            measurement_id.append(measurement)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            measurement_id.append("new row")
            for col in range(11, len(data.columns)-1,788):
                measurement_id_segment = list(data.values[elem, col:col+2])
                measurement_id_segment.reverse()
                measurement_id_segment = [int(elem) for index, elem in enumerate(measurement_id_segment)]
                measurement = int("".join(map(str, measurement_id_segment)))
                measurement_id.append(measurement)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            measurement_id.append("new row")
            for col in range(11, len(data.columns)-1, 788):
                measurement_id_segment = list(data.values[row, col:col+2])
                measurement_id_segment.reverse()
                measurement_id_segment = [int(elem) for index, elem in enumerate(measurement_id_segment)]
                measurement = int("".join(map(str, measurement_id_segment)))
                measurement_id.append(measurement)

    return measurement_id


def get_encoder_count(*args, single_row=False, multiple_row=False, row_section=False):
    """
    Takes in row arguements and boolean values and returns the encoder count for those row(s).

    Parameters:

        single_row: boolean
            If this is set to true, output the encoder count for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the encoder count for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the encoder count for the row sections the user selected.

    Example:

        >>> get_encoder_count(0,single_row=True)
        >>> [7680, 76168, 770, 7788, 77176, 788, 7896, 78184, 7916, 79104, 79192, 8024, 80112, 80200, 8132, 81120]

    Return:
    
        An array of all the encoder count the user desired to read.
    """
    
    encoder_count = []
    arg = [*args]

    print("NOTE: Each element is a encoder count for single azimuth block")
    if single_row is True:
        for col in range(13, len(data.columns)-1, 788):
            encoder_count_segment = list(data.values[arg[0], col:col+4])
            encoder_count_segment.reverse()
            encoder_count_segment = [int(elem) for index, elem in enumerate(encoder_count_segment)]
            encoder = int("".join(map(str, encoder_count_segment)))
            encoder_count.append(encoder)

    elif multiple_row is True:
        for index, elem in enumerate(arg):
            encoder_count.append('new row')
            for col in range(13, len(data.columns)-1, 788):
                encoder_count_segment = list(data.values[elem, col:col+4])
                encoder_count_segment.reverse()
                encoder_count_segment = [int(elem) for index, elem in enumerate(encoder_count_segment)]
                encoder = int("".join(map(str, encoder_count_segment)))
                encoder_count.append(encoder)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            encoder_count.append('new row')
            for col in range(13, len(data.columns)-1, 788):
                encoder_count_segment = list(data.values[elem, col:col+4])
                encoder_count_segment.reverse()
                encoder_count_segment = [int(elem) for index, elem in enumerate(encoder_count_segment)]
                encoder = int("".join(map(str, encoder_count_segment)))
                encoder_count.append(encoder)
                
    return encoder_count


def get_range(*args, single_row=False, multiple_row=False, row_section=False, azimuth_block=0):
    """
    Takes in row arguements, azimuth block number and boolean values and returns the range for those row(s)'s specified
    azimuth block.

    Parameters:

        azimuth_block: int
            Specifies which azimuth to read range values from.
        single_row: boolean
            If this is set to true, output the range for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the range for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the erange for the row sections the user selected.

    Example:

        >>> get_range(0,single_row=True,azimuth_block=1)
        >>> [128100, 0, 0, 0, 198100, 0, 16, 0, 38100, 0, 32, 0, 0, 32, 0, 0, 0, 32, 0, 0, 0, 0, 0, 16, 0, 0, 32, 0, 18740, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 32, 0, 0, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0]

    Return:
    
        An array of all the range the user desired to read.
    """
    range_mm = []
    arg = [*args]

    print("NOTE: Each element is a range in millimeters for single channel in azimuth block")
    if single_row is True:
        for col in (range(16+azimuth_block, azimuth_block+784, 12)):
            range_segment = list(data.values[args[0], col:col+3])
            range_segment = [int(elem) for index, elem in enumerate(range_segment)]
            rang = int("".join(map(str, range_segment)))
            range_mm.append(rang)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            range_mm.append('new row')
            for col in (range(16+azimuth_block, azimuth_block+784, 12)):
                range_segment = list(data.values[elem, col:col+3])
                range_segment = [int(elem) for index, elem in enumerate(range_segment)]
                rang = int("".join(map(str, range_segment)))
                range_mm.append(rang)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            range_mm.append('new row')
            for col in (range(16+azimuth_block, azimuth_block+784, 12)):
                range_segment = list(data.values[row, col:col+3])
                range_segment = [int(elem) for index, elem in enumerate(range_segment)]
                rang = int("".join(map(str, range_segment)))
                range_mm.append(rang)

    return range_mm


def get_reflectivity(*args, single_row=False, multiple_row=False, row_section=False, azimuth_block=0):
    """
    Takes in row arguements, azimuth block number and boolean values and returns the reflectivity for those row(s)'s specified
    azimuth block.

    Parameters:

        azimuth_block: int
            Specifies which azimuth to read reflectivity values from.
        single_row: boolean
            If this is set to true, output the reflectivity for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the reflectivity for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the reflectivity for the row sections the user selected.

    Example:

        >>> get_reflectivity(0,single_row=True,azimuth_block=1)
        >>> [190, 0, 0, 0, 360, 0, 0, 0, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    Return:
    
        An array of all the reflectivity the user desired to read.
    """
    reflectivity = []
    arg = [*args]

    print("NOTE: Each element is a reflectivity for single channel in azimuth block")
    if single_row is True:
        for col in (range(20+azimuth_block, azimuth_block+784, 12)):
            reflectivity_segment = list(data.values[args[0], col:col+2])
            reflectivity_segment = [int(elem) for index, elem in enumerate(reflectivity_segment)]
            reflect = int("".join(map(str, reflectivity_segment)))
            reflectivity.append(reflect)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            reflectivity.append('new row')
            for col in (range(20+azimuth_block, azimuth_block+784, 12)):
                reflectivity_segment = list(data.values[elem, col:col+2])
                reflectivity_segment = [int(elem) for index, elem in enumerate(reflectivity_segment)]
                reflect = int("".join(map(str, reflectivity_segment)))
                reflectivity.append(reflect)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            reflectivity.append('new row')
            for col in (range(20+azimuth_block, azimuth_block+784, 12)):
                reflectivity_segment = list(data.values[row, col:col+2])
                reflectivity_segment = [int(elem) for index, elem in enumerate(reflectivity_segment)]
                reflect = int("".join(map(str, reflectivity_segment)))
                reflectivity.append(reflect)

    return reflectivity


def get_signal_photons(*args, single_row=False, multiple_row=False, row_section=False, azimuth_block=0):
    """
    Takes in row arguements, azimuth block number and boolean values and returns the signal photons for those row(s)'s
    specified azimuth block.

    Parameters:

        azimuth_block: int
            Specifies which azimuth to read signal photons values from.
        single_row: boolean
            If this is set to true, output the signal photons for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the signal photons for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the signal photons for the row sections the user selected.

    Example:

        >>> get_signal_photons(0,single_row=True,azimuth_block=1)
        >>> [260, 0, 0, 0, 480, 0, 0, 0, 260, 0, 0, 0, 140, 0, 0, 0, 110, 0, 0, 0, 150, 0, 0, 0, 170, 0, 0, 0, 250, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    Return:
    
        An array of all the signal photons the user desired to read.
    """
    signal_photons = []
    arg = [*args]

    print("NOTE: Each element is a signal photon count for single channel in azimuth block")
    if single_row is True:
        for col in (range(22+azimuth_block, azimuth_block+784, 12)):
            signal_photons_segment = list(data.values[args[0], col:col+2])
            signal_photons_segment = [int(elem) for index, elem in enumerate(signal_photons_segment)]
            signal_p = int("".join(map(str, signal_photons_segment)))
            signal_photons.append(signal_p)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            signal_photons.append('new row')
            for col in (range(22+azimuth_block, azimuth_block+784, 12)):
                signal_photons_segment = list(data.values[elem, col:col+2])
                signal_photons_segment = [int(elem) for index, elem in enumerate(signal_photons_segment)]
                signal_p = int("".join(map(str, signal_photons_segment)))
                signal_photons.append(signal_p)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            signal_photons.append('new row')
            for col in (range(22+azimuth_block, azimuth_block+784, 12)):
                signal_photons_segment = list(data.values[row, col:col+2])
                signal_photons_segment = [int(elem) for index, elem in enumerate(signal_photons_segment)]
                signal_p = int("".join(map(str, signal_photons_segment)))
                signal_photons.append(signal_p)

    return signal_photons


def get_noise_photons(*args, single_row=False, multiple_row=False, row_section=False, azimuth_block=0):
    """
    Takes in row arguements, azimuth block number and boolean values and returns the noise photons for those row(s)'s
    specified azimuth block.

    Parameters:

        azimuth_block: int
            Specifies which azimuth to read noise photons values from.
        single_row: boolean
            If this is set to true, output the noise photons for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the noise photons for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the noise photons for the row sections the user selected.

    Example:

        >>> get_noise_photons(0,single_row=True,azimuth_block=1)
        >>> [14560, 36330, 12, 1291280, 17040, 4008, 19200, 12417616, 22740, 36016, 17719015, 6150, 20430, 100, 36932, 12878, 12140, 210222, 8024, 1321122, 23440, 1702540, 2261360, 21625515, 25430, 80, 2522481, 2480, 19620, 923915, 15048, 96638, 16470, 12814816, 7016, 2321781, 15360, 1720, 1286432, 2021, 18950, 287040, 1571120, 21417, 22030, 2417217, 126390, 192538, 50120, 1361288, 48, 942380, 1930, 12800, 41602, 2081240, 14740, 25514333, 406433, 9018, 24330, 84832, 167240, 200680]

    Return:
    
        An array of all the noise photons the user desired to read.
    """
    noise_photons = []
    arg = [*args]

    print("NOTE: Each element is a noise photon count for single channel in azimuth block")
    if single_row is True:
        for col in (range(24+azimuth_block, azimuth_block+788, 12)):
            noise_photons_segment = list(data.values[arg[0], col:col+3])
            noise_photons_segment = [int(elem) for index, elem in enumerate(noise_photons_segment)]
            noise_p = int("".join(map(str, noise_photons_segment)))
            noise_photons.append(noise_p)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            noise_photons.append('new row')
            for col in (range(24+azimuth_block, azimuth_block+788, 12)):
                noise_photons_segment = list(data.values[elem, col:col+3])
                noise_photons_segment = [int(elem) for index, elem in enumerate(noise_photons_segment)]
                noise_p = int("".join(map(str, noise_photons_segment)))
                noise_photons.append(noise_p)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            noise_photons.append('new row')
            for col in (range(24+azimuth_block, azimuth_block+788, 12)):
                noise_photons_segment = list(data.values[row, col:col+3])
                noise_photons_segment = [int(elem) for index, elem in enumerate(noise_photons_segment)]
                noise_p = int("".join(map(str, noise_photons_segment)))
                noise_photons.append(noise_p)

    return noise_photons


def get_packet_status(*args, single_row=False, multiple_row=False, row_section=False):
    """
    Takes in row arguements, azimuth block number and boolean values and returns the packet status for those row(s)'s
    specified azimuth block.

    Parameters:

        single_row: boolean
            If this is set to true, output the packet status for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the packet status for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the packet status for the row sections the user selected.

    Example:

        >>> get_packet_status(0,single_row=True)
        >>> 'packet is good'

    Return:
    
        An array of all the packet status the user desired to read.
        """
    packet_status = []
    arg = [*args]

    if single_row is True:
        for col in range(785, len(data.columns) - 1, 788):
            packet_status_segment = list(data.values[arg[0], col:col + 4])
            packet_status_segment.reverse()
            packet_status_segment = [int(elem) for index, elem in enumerate(packet_status_segment)]
            status = int("".join(map(str, packet_status_segment)))
            packet_status.append(status)

    elif multiple_row is True:
        for index, elem in enumerate(arg):
            packet_status.append('new row')
            for col in range(785, len(data.columns) - 1, 788):
                packet_status_segment = list(data.values[elem, col:col + 4])
                packet_status_segment.reverse()
                packet_status_segment = [int(elem) for index, elem in enumerate(packet_status_segment)]
                status = int("".join(map(str, packet_status_segment)))
                packet_status.append(status)
    elif row_section is True:
        for row in range(arg[0], arg[1] + 1):
            packet_status.append('new row')
            for col in range(785, len(data.columns) - 1, 788):
                packet_status_segment = list(data.values[row, col:col + 4])
                packet_status_segment.reverse()
                packet_status_segment = [int(elem) for index, elem in enumerate(packet_status_segment)]
                status = int("".join(map(str, packet_status_segment)))
                packet_status.append(status)

    if packet_status[len(packet_status)-1] == 255255255255:
        return 'packet is good'
