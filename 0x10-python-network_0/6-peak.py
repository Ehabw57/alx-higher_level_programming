#!/usr/bin/python3
"""A script of function find_peak"""


def find_peak(ints):
    """Finds a peak in a list of ints"""
    if len(ints) < 1:
        return None

    n = len(ints) // 2
    try:
        if (ints[n] >= ints[n+1] and ints[n] >= ints[-1]):
            return ints[n]
        else:
            peak = find_peak(ints[n:])
    except IndexError:
        return None

    if (peak is not None):
        return peak
    else:
        find_peak(ints[0:n])
