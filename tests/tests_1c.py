"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_first_element_positive():                      # Test whether the first element in an array is positive 
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray_sum([1]) == 1
    assert max_subarray_sum([5, 4, -1, 7, 8]) == 23

def test_first_element_negative():                     # Test whether the first element in an array is negative
    assert max_subarray_sum([-1]) == -1
    assert max_subarray_sum([-2, 1]) == 1               # All sums are negative, except [1]
    assert max_subarray_sum([-2, -1]) == -1             # All elements are negative

if __name__ == "__main__":
    pytest.main()