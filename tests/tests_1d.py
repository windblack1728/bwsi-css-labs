"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum


def test_working():                                       # Testing whether it works
    assert two_sum([2,7,11,15], 9) in [[0, 1], [1, 0]]
    assert two_sum([3, 2, 4], 6) in [[1, 2], [2, 1]]
    assert two_sum([3, 3], 6) in [[0, 1], [1, 0]]
    assert two_sum([3, 2, 3], 6) in [[0, 2], [2, 0]]
    assert two_sum([19, 1, 18, 3, 16, 4, 13, 9, 11], 21) in [[2, 3], [3, 2]]

if __name__ == "__main__":
    pytest.main()