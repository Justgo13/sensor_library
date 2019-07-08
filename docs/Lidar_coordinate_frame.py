from lidar_extract import *
import math


def set_range(row_num, azimuth_block, channel_num):
    """
    Gets the range value from the desired row,azimuth block and channel.

    Parameter:

        row_num: int
            The number of the desired row to extract range from.
        azimuth_block: int
            The number of the desired azimuth block to extract range from.
        channel_num: int
            The number of the desired channel num to extract range from.

    Example:

        >>> set_range(0,1,0)
        >>> 128100

    Return:
        Range value in millimeters for that desired row, azimuth block and channel number.
    """
    range_mm = get_range(row_num, single_row=True, azimuth_block=azimuth_block)[channel_num]

    return range_mm


def set_encoder(row_num, azimuth_block):
    """
    Gets the encoder count from the desired row,azimuth block.

    Parameter:

        row_num: int
            The number of the desired encoder count to extract range from.
        azimuth_block: int
            The number of the desired encoder count azimuth block to extract range from.

    Example:

        >>> set_encoder(0,1,0)
        >>> 76168

    Return:
        Encoder count of desired row, azimuth block.
    """
    encoder_count = get_encoder_count(row_num, single_row=True)[azimuth_block]

    return encoder_count


def set_beam_altitude_angle(channel_num):
    """
    Returns the beam altitude angle of the specified channel number.

    Example:

        >>> set_beam_altitude_angle(0)
        >>> 16.923
    """
    beam_altitude_angle=[16.923, 16.311, 15.739, 15.192, 14.7, 14.139, 13.578, 13.033, 12.573, 11.994, 11.453, 10.909, 10.45, 9.883, 9.341,
                         8.803, 8.343, 7.787, 7.241, 6.702, 6.253, 5.695, 5.157, 4.604, 4.168, 3.608, 3.061, 2.523, 2.071, 1.529, 0.976, 0.428,
                         -0.031, -0.573, -1.189, -1.664, -2.116, -2.656, -3.204, -3.759, -4.209, -4.751, -5.301, -5.857, -6.31, -6.845, -7.394,
                         -7.957, -8.403, -8.939, -9.494, -10.06, -10.51, -11.052, -11.609, -12.181, -12.632, -13.171, -13.74, -14.321, -14.785,
                         -15.333, -15.9, -16.498]

    return beam_altitude_angle[channel_num]


def set_beam_azimuth_angle(channel_num):
    """
    Returns the beam azimuth anlge of the specified channel number.

    Example:

        >>> set_beam_azimuth_angle(0)
        >>> 3.069
    """
    beam_azimuth_angles=[3.069, 0.905, -1.25, -3.382, 3.055, 0.913, -1.207, -3.327, 3.047, 0.923, -1.188, -3.286, 3.051, 0.954, -1.161, -3.246,
                         3.05, 0.966, -1.124, -3.194, 3.063, 0.979, -1.102, -3.167, 3.081, 1.007, -1.069, -3.142, 3.103, 1.032, -1.042, -3.118,
                         3.123, 1.058, -1.072, -3.089, 3.145, 1.081, -0.991, -3.071, 3.183, 1.109, -0.968, -3.056, 3.212, 1.132, -0.951, -3.039,
                         3.25, 1.166, -0.933, -3.041, 3.292, 1.189, -0.908, -3.023, 3.347, 1.232, -0.892, -3.026, 3.405, 1.271, -0.868, -3.026]

    return beam_azimuth_angles[channel_num]


def get_theta(row_num, azimuth_block, channel_num):
    """
    Calculates the angle theta given row number, azimuth block number and channel number.

    Parameter:

        row_num: int
            The number of the desired row to be used to find encoder count for that row.
        azimuth_block: int
            The number of the desired azimuth block to be used to find encoder count for that row.
        channel_num: int
            The number of the desired channel num to be used to find encoder count for that row.

    Example:

        >>> get_theta(0,1,0)
        >>> 5.364484548001593

    Return:

        An angle theta in radians.
    """
    theta = 2*math.pi*(set_encoder(row_num, azimuth_block)/90112 + set_beam_azimuth_angle(channel_num)/360)

    return theta


def get_phi(channel_num):
    """
    Calculates the angle phi given channel number.

    Parameter:

        channel_num: int
            The number of the desired row's channel number to extract range from.

    Example:

        >>> get_phi(0)
        >>> 0.29536206931500036

    Returns:

        An angle phi in radians.
    """
    phi = (2*math.pi*set_beam_altitude_angle(channel_num))/360

    return phi


def get_x(row_num, azimuth_block, channel_num):
    """
    Returns the x coordinate of the data point passed in.

    Example:

        >>> get_x(0,1,0)
        >>> 74371.6113033144
    """
    x = set_range(row_num, azimuth_block, channel_num)*math.cos(get_theta(row_num, azimuth_block, channel_num))*math.cos(get_phi(channel_num))

    return x


def get_y(row_num, azimuth_block, channel_num):
    """
    Returns the y coordinate of the data point passed in.

    Example:

        >>> get_y(0,1,0)
        >>> 97406.71081129464
    """
    y = -1*set_range(row_num, azimuth_block, channel_num)*math.sin(get_theta(row_num, azimuth_block, channel_num))*math.cos(get_phi(channel_num))

    return y


def get_z(row_num, azimuth_block, channel_num):
    """
    Returns the z coordinate of the data point passed in.

    Example:

        >>> get_z(0,1,0)
        >>> 37288.149874638875
    """
    z = set_range(row_num, azimuth_block, channel_num)*math.sin(get_phi(channel_num))

    return z