"""Unit Test for Ex05."""
__author__ = "730551547"

from exercises.ex05.utils import only_evens, sub, concat


def test_empty_only_evens() -> None:
    """Testing empty string for only_evens."""
    numberlist: list[int] = []
    assert only_evens(numberlist) == []


def test_negative_only_evens() -> None:
    """Testing negative string elements for only_evens."""
    numberlist: list[int] = [-2, -5, -6]
    assert only_evens(numberlist) == [-2, -6]


def test_many_only_evens() -> None:
    """Testing multiple elements in a string for evens."""
    numberlist: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(numberlist) == [2, 4]


def test_empty_concat() -> None:
    """Testing empty string for concat."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def test_negative_concat() -> None:
    """Testing empty string for concat."""
    list1: list[int] = [-2, -3]
    list2: list[int] = [-4, -5]
    assert concat(list1, list2) == [-2, -3, -4, -5]


def test_many_concat() -> None:
    """Testing empty string for concat."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5]
    assert concat(list1, list2) == [1, 2, 3, 4, 5]


def test_empty_sub() -> None:
    """Testing empty string for sub."""
    a_list: list[int] = []
    sindex: int = 0
    eindex: int = 0
    assert sub(a_list, sindex, eindex) == []


def test_negatives_sub() -> None:
    """Testing negative elements in a string for sub."""
    a_list: list[int] = [-2, -3, -4, -5]
    assert sub(a_list) == [-3, -4]


def test_many_sub() -> None:
    """Testing many elements in a string for sub."""
    a_list: list[int] = [2, 3, 4, 5, 6, 7]
    sindex: int = 2
    eindex: int = 4
    assert sub(a_list, sindex, eindex) == [4, 5]