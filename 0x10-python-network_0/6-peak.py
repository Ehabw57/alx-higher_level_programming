#!/usr/bin/python3
"""Hehe find the peak moudel"""


def find_peak(list_of_integers):
    """Finds a peak in a list of ints"""
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
