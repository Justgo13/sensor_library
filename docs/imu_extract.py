import pandas as pd

file = "imu_data3.csv"
data = pd.read_csv(file)


def get_IMU_time(*args, single_row=False, multiple_row=False, row_section=False):
    """
    Takes in the desired row(s) to be read and returns the IMU timestamp.

    Parameters:

        single_row: boolean
            If this is set to true, output the IMU timestamp for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the IMU timestamp for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the IMU timestamp for the row sections the user selected.

    Example:

        >>> get_IMU_time(0,single_row=True)
        >>> [34.01298918023]

    Return:

        A single element array of the timestamp values in seconds.
    """
    IMU_time = []
    arg = [*args]
    
    print("NOTE: All timestamps measured in seconds")
    if single_row is True:
        IMU_time_segment = list(data.values[arg[0], 1:9])
        IMU_time_segment.reverse()
        IMU_time_segment = [int(elem) for index, elem in enumerate(IMU_time_segment)]
        del IMU_time_segment[0:3]
        IMU_time_segment[0] = float(IMU_time_segment[0])
        IMU = float("".join(map(str, IMU_time_segment)))
        IMU_time.append(IMU)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            IMU_time.append('new row')
            IMU_time_segment = list(data.values[elem, 1:9])
            IMU_time_segment.reverse()
            IMU_time_segment = [int(elem) for index, elem in enumerate(IMU_time_segment)]
            del IMU_time_segment[0:3]
            IMU_time_segment[0] = float(IMU_time_segment[0])
            IMU = float("".join(map(str, IMU_time_segment)))
            IMU_time.append(IMU)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            IMU_time.append('new row')
            IMU_time_segment = list(data.values[row, 1:9])
            IMU_time_segment.reverse()
            IMU_time_segment = [int(elem) for index, elem in enumerate(IMU_time_segment)]
            del IMU_time_segment[0:3]
            IMU_time_segment[0] = float(IMU_time_segment[0])
            IMU = float("".join(map(str, IMU_time_segment)))
            IMU_time.append(IMU)
            
    return IMU_time


def get_accel_time(*args, single_row=False, multiple_row=False, row_section=False):
    """
    Takes in the desired row(s) to be read and returns the accelerometer timestamp.

    Parameters:

        single_row: boolean
            If this is set to true, output the accelerometer timestamp for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the accelerometer timestamp for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the accelerometer timestamp for the row sections the user selected.

    Example:

        >>> get_accel_time(0,single_row=True)
        >>> [33.04112810818]

    Return:

        A single element array of the timestamp values in seconds.
    """
    accel_time = []
    arg = [*args]
    
    if single_row is True:
        accel_time_segment = list(data.values[arg[0], 9:17])
        accel_time_segment.reverse()
        accel_time_segment = [int(elem) for index, elem in enumerate(accel_time_segment)]
        del accel_time_segment[0:3]
        accel_time_segment[0] = float(accel_time_segment[0])
        accel = float("".join(map(str, accel_time_segment)))
        accel_time.append(accel)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            accel_time.append('new row')
            accel_time_segment = list(data.values[elem, 9:17])
            accel_time_segment.reverse()
            accel_time_segment = [int(elem) for index, elem in enumerate(accel_time_segment)]
            del accel_time_segment[0:3]
            accel_time_segment[0] = float(accel_time_segment[0])
            accel = float("".join(map(str, accel_time_segment)))
            accel_time.append(accel)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            accel_time.append('new row')
            accel_time_segment = list(data.values[row, 9:17])
            accel_time_segment.reverse()
            accel_time_segment = [int(elem) for index, elem in enumerate(accel_time_segment)]
            del accel_time_segment[0:3]
            accel_time_segment[0] = float(accel_time_segment[0])
            accel = float("".join(map(str, accel_time_segment)))
            accel_time.append(accel)
            
    return accel_time


def get_gyro_time(*args, single_row=False, multiple_row=False, row_section=False):
    """
    Takes in the desired row(s) to be read and returns the gyroscope timestamp.

    Parameters:

        single_row: boolean
            If this is set to true, output the gyroscope timestamp for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the gyroscope timestamp for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the gyroscope timestamp for the row sections the user selected.

    Example：

        >>> get_gyro_time(0,single_row=True)
        >>> [33.04111484188]

    Return:

        A single element array of the timestamp values in seconds.
    """
    gyro_time = []
    arg = [*args]
    
    if single_row is True:
        gyro_time_segment = list(data.values[arg[0], 17:25])
        gyro_time_segment.reverse()
        gyro_time_segment = [int(elem) for index, elem in enumerate(gyro_time_segment)]
        del gyro_time_segment[0:3]
        gyro_time_segment[0] = float(gyro_time_segment[0])
        gyro = float("".join(map(str, gyro_time_segment)))
        gyro_time.append(gyro)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            gyro_time.append('new row')
            gyro_time_segment = list(data.values[elem, 17:25])
            gyro_time_segment.reverse()
            gyro_time_segment = [int(elem) for index, elem in enumerate(gyro_time_segment)]
            del gyro_time_segment[0:3]
            gyro_time_segment[0] = float(gyro_time_segment[0])
            gyro = float("".join(map(str, gyro_time_segment)))
            gyro_time.append(gyro)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            gyro_time.append('new row')
            gyro_time_segment = list(data.values[row, 17:25])
            gyro_time_segment.reverse()
            gyro_time_segment = [int(elem) for index, elem in enumerate(gyro_time_segment)]
            del gyro_time_segment[0:3]
            gyro_time_segment[0] = float(gyro_time_segment[0])
            gyro = float("".join(map(str, gyro_time_segment)))
            gyro_time.append(gyro)
            
    return gyro_time


def get_x_accel(*args, single_row=False, multiple_row=False, row_section=False):
    """
    Takes in the desired row(s) to be read and returns the x acceleration.

    Parameters:

        single_row: boolean
            If this is set to true, output the x acceleration for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the x acceleration for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the x acceleration for the row sections the user selected.

    Example:

        >>> get_x_accel(0,single_row=True)
        >>> [615900]

    Return:

        A single element array of the x acceleration values in seconds.
    """
    x_accel = []
    arg = [*args]
    
    if single_row is True:
        x_accel_segment = list(data.values[arg[0], 25:29])
        x_accel_segment.reverse()
        x = int("".join(map(str, x_accel_segment)))
        x_accel.append(x)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            x_accel.append('new row')
            x_accel_segment = list(data.values[elem, 25:29])
            x_accel_segment.reverse()
            x = int("".join(map(str, x_accel_segment)))
            x_accel.append(x)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            x_accel.append('new row')
            x_accel_segment = list(data.values[row, 25:29])
            x_accel_segment.reverse()
            x = int("".join(map(str, x_accel_segment)))
            x_accel.append(x)
            
    return x_accel


def get_y_accel(*args, single_row=False, multiple_row=False, row_section=False):
    """
    Takes in the desired row(s) to be read and returns the y acceleration.

    Parameters:

        single_row: boolean
            If this is set to true, output the y acceleration for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the y acceleration for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the y acceleration for the row sections the user selected.

    Example:

        >>> get_y_accel(0,single_row=True)
        >>> [1896900]

    Return:

        A single element array of the y acceleration values in seconds.
    """
    y_accel = []
    arg = [*args]
    
    if single_row is True:
        y_accel_segment = list(data.values[arg[0], 29:33])
        y_accel_segment.reverse()
        y = int("".join(map(str, y_accel_segment)))
        y_accel.append(y)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            y_accel.append('new row')
            y_accel_segment = list(data.values[elem, 29:33])
            y_accel_segment.reverse()
            y = int("".join(map(str, y_accel_segment)))
            y_accel.append(y)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            y_accel.append('new row')
            y_accel_segment = list(data.values[row, 29:33])
            y_accel_segment.reverse()
            y = int("".join(map(str, y_accel_segment)))
            y_accel.append(y)
            
    return y_accel


def get_z_accel(*args, single_row=False, multiple_row=False, row_section=False):
    """
    Takes in the desired row(s) to be read and returns the z acceleration.

    Parameters:

        single_row: boolean
            If this is set to true, output the z acceleration for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the z acceleration for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the z acceleration for the row sections the user selected.

    Example:

        >>> get_z_accel(0,single_row=True)
        >>> [191125320]

    Return:

        A single element array of the z acceleration values in seconds.
    """
    z_accel = []
    arg = [*args]
    
    if single_row is True:
        z_accel_segment = list(data.values[arg[0], 33:37])
        z_accel_segment.reverse()
        z = int("".join(map(str, z_accel_segment)))
        z_accel.append(z)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            z_accel.append('new row')
            z_accel_segment = list(data.values[elem, 33:37])
            z_accel_segment.reverse()
            z = int("".join(map(str, z_accel_segment)))
            z_accel.append(z)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            z_accel.append('new row')
            z_accel_segment = list(data.values[row, 33:37])
            z_accel_segment.reverse()
            z = int("".join(map(str, z_accel_segment)))
            z_accel.append(z)
            
    return z_accel


def get_x_ang_vel(*args, single_row=False, multiple_row=False, row_section=False):
    """
    Takes in the desired row(s) to be read and returns the x angular acceleration.

    Parameters:

        single_row: boolean
            If this is set to true, output the x angular acceleration for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the x angular acceleration for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the x angular acceleration for the row sections the user selected.

    Example:

        >>> get_x_accel(0,single_row=True)
        >>> [191551520]

    Return:

        A single element array of the x angular acceleration values in seconds.
    """
    x_ang_vel = []
    arg = [*args]
    
    if single_row is True:
        x_ang_vel_segment = list(data.values[arg[0], 37:41])
        x_ang_vel_segment.reverse()
        x_ang = int("".join(map(str, x_ang_vel_segment)))
        x_ang_vel.append(x_ang)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            x_ang_vel.append('new row')
            x_ang_vel_segment = list(data.values[elem, 37:41])
            x_ang_vel_segment.reverse()
            x_ang = int("".join(map(str, x_ang_vel_segment)))
            x_ang_vel.append(x_ang)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            x_ang_vel.append('new row')
            x_ang_vel_segment = list(data.values[row, 37:41])
            x_ang_vel_segment.reverse()
            x_ang = int("".join(map(str, x_ang_vel_segment)))
            x_ang_vel.append(x_ang)
            
    return x_ang_vel


def get_y_ang_vel(*args, single_row=False, multiple_row=False, row_section=False):
    """
    Takes in the desired row(s) to be read and returns the y angular acceleration.
    Parameters:

        single_row: boolean
            If this is set to true, output the y angular acceleration for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the y angular acceleration for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the y angular acceleration for the row sections the user selected.

    Example:

        >>> get_y_ang_vel(0,single_row=True)
        >>> [189203320]

    Return:

        A single element array of the y angular acceleration values in seconds.
    """
    y_ang_vel = []
    arg = [*args]
    
    if single_row is True:
        y_ang_vel_segment = list(data.values[arg[0], 41:45])
        y_ang_vel_segment.reverse()
        y_ang = int("".join(map(str, y_ang_vel_segment)))
        y_ang_vel.append(y_ang)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            y_ang_vel.append('new row')
            y_ang_vel_segment = list(data.values[elem, 41:45])
            y_ang_vel_segment.reverse()
            y_ang = int("".join(map(str, y_ang_vel_segment)))
            y_ang_vel.append(y_ang)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            y_ang_vel.append('new row')
            y_ang_vel_segment = list(data.values[row, 41:45])
            y_ang_vel_segment.reverse()
            y_ang = int("".join(map(str, y_ang_vel_segment)))
            y_ang_vel.append(y_ang)
            
    return y_ang_vel


def get_z_ang_vel(*args, single_row=False, multiple_row=False, row_section=False):
    """
    Takes in the desired row(s) to be read and returns the z angular acceleration.
    Parameters:

        single_row: boolean
            If this is set to true, output the z angular acceleration for the row that the user selected.
        multiple_row: boolean
            If this is set to true, output the z angular acceleration for the rows that the user selected.
        row_section: boolean
            If this is set to true, output the z angular acceleration for the row sections the user selected.

    Example:

        >>> get_z_ang_vel(0,single_row=True)
        >>> [189203320]

    Return:

        A single element array of the z angular acceleration values in seconds.
    """
    z_ang_vel = []
    arg = [*args]
    
    if single_row is True:
        z_ang_vel_segment = list(data.values[arg[0], 41:45])
        z_ang_vel_segment.reverse()
        z_ang = int("".join(map(str, z_ang_vel_segment)))
        z_ang_vel.append(z_ang)
    elif multiple_row is True:
        for index, elem in enumerate(arg):
            z_ang_vel.append('new row')
            z_ang_vel_segment = list(data.values[elem, 41:45])
            z_ang_vel_segment.reverse()
            z_ang = int("".join(map(str, z_ang_vel_segment)))
            z_ang_vel.append(z_ang)
    elif row_section is True:
        for row in range(arg[0], arg[1]+1):
            z_ang_vel.append('new row')
            z_ang_vel_segment = list(data.values[row, 41:45])
            z_ang_vel_segment.reverse()
            z_ang = int("".join(map(str, z_ang_vel_segment)))
            z_ang_vel.append(z_ang)
            
    return z_ang_vel