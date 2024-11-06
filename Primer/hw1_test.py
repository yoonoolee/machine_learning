"""
Avery Lee
CSE 163 AB
This program implements the test functions for hw1.py
"""


import hw1

from cse163_utils import assert_equals


def test_total():
    """
    Tests the total method
    """
    # The regular case
    assert_equals(15, hw1.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw1.total(1))
    assert_equals(0, hw1.total(0))

    # Test the None case
    assert_equals(None, hw1.total(-1))


def test_count_divisible_digits():
    """
    Tests the count_divisible_digits method
    """
    # given
    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    assert_equals(0, hw1.count_divisible_digits(24, 5))
    assert_equals(0, hw1.count_divisible_digits(1, 0))
    # my own
    assert_equals(1, hw1.count_divisible_digits(-1, 1))
    assert_equals(1, hw1.count_divisible_digits(2, 2))


def test_is_relatively_prime():
    """
    Tests the is_relatively_prime method
    """
    # given
    assert_equals(True, hw1.is_relatively_prime(12, 13))
    assert_equals(False, hw1.is_relatively_prime(12, 14))
    assert_equals(True, hw1.is_relatively_prime(5, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 1))
    # my own
    assert_equals(False, hw1.is_relatively_prime(8, 12))
    assert_equals(True, hw1.is_relatively_prime(1, 1))


def test_travel():
    """
    Tests the travel method
    """
    # given
    assert_equals((-1, 4), hw1.travel('NW!ewnW', 1, 2))
    # my own
    assert_equals((0, 0), hw1.travel('enaws', 0, 0))
    assert_equals((1, 1), hw1.travel('', 1, 1))


def test_compress():
    """
    Tests the compress method
    """
    # given
    assert_equals('c1o17l1k1a1n1g1a1r1o2',
                  hw1.compress('cooooooooooooooooolkangaroo'))
    assert_equals('a3', hw1.compress('aaa'))
    assert_equals('', hw1.compress(''))
    # my own
    assert_equals('a1b1a1b1a1b1', hw1.compress('ababab'))
    assert_equals('A1a1B1b1', hw1.compress('AaBb'))


def test_longest_word():
    """
    Tests the longest_word method
    """
    # given
    assert_equals('3: Merrily,', hw1.longest_word('/home/song.txt'))
    # my own
    assert_equals('1: Twinkle,', hw1.longest_word('/home/song2.txt'))
    assert_equals('2: hijklmnop', hw1.longest_word('/home/song3.txt'))


def test_get_average_in_range():
    """
    Tests the get_average_in_range method
    """
    # given
    assert_equals(5.5, hw1.get_average_in_range([1, 5, 6, 7, 9], 5, 7))
    assert_equals(2.0, hw1.get_average_in_range([1, 2, 3], -1, 10))
    # my own
    assert_equals(3.75, hw1.get_average_in_range([1, 2, 3, 9], -1, 10))
    assert_equals(1.0, hw1.get_average_in_range([1, 2], 1, 2))


def test_mode_digit():
    """
    Tests the mode_digit() method
    """
    # given
    assert_equals(1, hw1.mode_digit(12121))
    assert_equals(0, hw1.mode_digit(0))
    assert_equals(2, hw1.mode_digit(-122))
    assert_equals(2, hw1.mode_digit(1211232231))
    # my own
    assert_equals(3, hw1.mode_digit(112233))
    assert_equals(0, hw1.mode_digit(1000))


def main():
    test_total()
    # Call your test functions here!
    test_count_divisible_digits()
    test_is_relatively_prime()
    test_travel()
    test_compress()
    test_longest_word()
    test_get_average_in_range()
    test_mode_digit()


if __name__ == '__main__':
    main()
