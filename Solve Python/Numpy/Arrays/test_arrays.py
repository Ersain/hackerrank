import numpy as np
from Arrays import reverse_array


def test_arrays_1():
    assert all(reverse_array(np.array([1, 2, 3, 4])) == np.array([4, 3, 2, 1]))


def test_arrays_2():
    assert all(reverse_array(
        np.array([5, 4, 8, 2, 1, 8])) == np.array([8, 1, 2, 8, 4, 5]))


def test_arrays_3():
    assert all(reverse_array(np.array([9, 8, 7, 6, 5, 4, 3, 2, 1])) == np.array(
        [1, 2, 3, 4, 5, 6, 7, 8, 9]))
