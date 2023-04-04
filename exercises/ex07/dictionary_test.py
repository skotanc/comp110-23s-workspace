"""EX07 - Dictionary Functions Test."""
__author__ = "730551547"

from dictionary import invert, favorite_color, count
import pytest


def test_error() -> None:
    """Return keyerror if there are repeated occurences of the same."""
    with pytest.raises(KeyError):
        input: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
        invert(input)


def test_empty_invert() -> None:
    """Testing an empty dictionary."""
    input: dict[str, str] = {}
    assert invert(input) == {}


def test_int_invert() -> None:
    """Testing a dictionary with integer values."""
    input: dict[str, str] = {'1': '3', '5': '7', '4': '6'}
    assert invert(input) == {'3': '1', '7': '5', '6': '4'}


def test_both_invert() -> None:
    """Testing a dictionary with integer and string values."""
    input: dict[str, str] = {'a': '3', 'b': '7', 'c': '6'}
    assert invert(input) == {'3': 'a', '7': 'b', '6': 'c'}


def test_str_invert() -> None:
    """Testing a dictionary with string values."""
    input: dict[str, str] = {'eyecolor': 'brown', 'haircolor': 'black', 'shirtcolor': 'blue'}
    assert invert(input) == {'brown': 'eyecolor', 'black': 'haircolor', 'blue': 'shirtcolor'}


def test_empty_favorite_color() -> None:
    """Testing a dictionary with empty values."""
    input: dict[str, str] = {}
    assert favorite_color(input) == {}


def test_one_favorite_color() -> None:
    """Testing a dictionary with one value."""
    input: dict[str, str] = {'Shreya': 'blue'}
    assert favorite_color(input) == 'blue'


def test_many_favorite_color() -> None:
    """Testing a dictionary with many values."""
    input: dict[str, str] = {'Shreya': 'blue', 'Steve': 'yellow', 'Rose': 'yellow'}
    assert favorite_color(input) == 'yellow'


def test_same_favorite_color() -> None:
    """Testing a dictionary with many values with the same color."""
    input: dict[str, str] = {'Shreya': 'blue', 'Steve': 'blue', 'Rose': 'blue'}
    assert favorite_color(input) == 'blue'


def test_empty_count() -> None:
    """Testing an empty list."""
    input: list[str] = []
    assert count(input) == {}


def test_one_count() -> None:
    """Testing a dictionary with one value."""
    input: list[str] = ['3']
    assert count(input) == {'3': 1}


def test_many_count() -> None:
    """Testing a dictionary with many values."""
    input: list[str] = ['3', '2', '3', '4', '4', '3']
    assert count(input) == {'3': 3, '2': 1, '4': 2}


def test_negative_count() -> None:
    """Testing a dictionary with negative values."""
    input: list[str] = ['-1', '-2', '-2', '-2', '-2', '-5', '-2', '-5']
    assert count(input) == {'-1': 1, '-2': 5, '-5': 2}