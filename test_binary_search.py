from binary_search import binary_search
from binary_search import recursive_binary_search


def test_bs_value_found():
    array = [3, 6, 9, 20, 33, 50, 62, 91]
    value = 9
    assert binary_search(array, value) == 1


def test_bs_value_not_found():
    array = [3, 6, 9, 20, 33, 50, 62, 91]
    value = 5
    assert binary_search(array, value) == 0


def test_rsbs_value_found():
    array = [3, 6, 9, 20, 33, 50, 62, 91]
    value = 9
    assert recursive_binary_search(array, value) == 1


def test_rsbs_value_not_found():
    array = [3, 6, 9, 20, 33, 50, 62, 91]
    value = 5
    assert recursive_binary_search(array, value) == 0
