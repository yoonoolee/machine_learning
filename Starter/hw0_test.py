"""
Avery Lee
CSE 163 AB
This program tests hw0.py functions
"""

import hw0

from cse163_utils import assert_equals


def test_total():
    """
    tests function total()
    """
    # The regular case
    assert_equals(15, hw0.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw0.total(1))
    assert_equals(0, hw0.total(0))
    # task
    assert_equals(None, hw0.total(-1))  # check negative n


def test_funky_sum():
    """
    tests function funky_sum()
    """
    # my test cases
    assert_equals(1, hw0.funky_sum(1, 2, 0))
    assert_equals(1, hw0.funky_sum(1, 2, -1))
    assert_equals(2, hw0.funky_sum(1, 2, 1))
    assert_equals(2, hw0.funky_sum(1, 2, 2))
    assert_equals(1.5, hw0.funky_sum(1, 2, 0.5))
    # given test cases
    assert_equals(2.0, hw0.funky_sum(1, 3, 0.5))
    assert_equals(1.0, hw0.funky_sum(1, 3, 0))
    assert_equals(1.5, hw0.funky_sum(1, 3, 0.25))
    assert_equals(2.2, hw0.funky_sum(1, 3, 0.6))
    assert_equals(3.0, hw0.funky_sum(1, 3, 1))


def test_swip_swap():
    """
    tests function swip_swap()
    """
    # my test cases
    assert_equals('holle', hw0.swip_swap('hello', 'e', 'o'))
    assert_equals('hellz', hw0.swip_swap('hello', 'z', 'o'))
    # given test cases
    assert_equals('offbar', hw0.swip_swap('foobar', 'f', 'o'))
    assert_equals('foocar', hw0.swip_swap('foobar', 'b', 'c'))


def main():
    test_total()
    test_funky_sum()
    test_swip_swap()


if __name__ == '__main__':
    main()
