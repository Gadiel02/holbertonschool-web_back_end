#!/usr/bin/env python3
"""
This is a module that provides a function for summing list values.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Sums up all the float values in a list.

    Args:
        input_list (List[float]): A list of float numbers to be summed.

    Returns:
        float: The sum of all the numbers in the input list.
    """
    return sum(input_list)
