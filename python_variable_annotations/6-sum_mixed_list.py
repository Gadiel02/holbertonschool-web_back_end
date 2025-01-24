#!/usr/bin/env python3
"""
This module provides a function for summing a mixed list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums up all the integer and float values in a list.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and floats.

    Returns:
        float: The sum of all the numbers in the list as a float.
    """
    return sum(mxd_lst)
