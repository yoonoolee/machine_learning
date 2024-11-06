"""Avery Lee
CSE 163 AB
This program implements the test functions for HW2
"""


from cse163_utils import assert_equals, parse

import pandas as pd
import hw2_manual
import hw2_pandas


# Your tests here!
def test_species_count(test1_parse, test2_parse, test1_pandas, test2_pandas):
    """
    Tests the species_count method
    """
    # given (test1)
    assert_equals(3, hw2_manual.species_count(test1_parse))
    assert_equals(3, hw2_pandas.species_count(test1_pandas))
    # my own (test2)
    assert_equals(4, hw2_manual.species_count(test2_parse))
    assert_equals(4, hw2_pandas.species_count(test2_pandas))


def test_max_level(test1_parse, test2_parse, test1_pandas, test2_pandas):
    """
    Tests the max_level method
    """
    # given (test1)
    assert_equals(('Lapras', 72), hw2_manual.max_level(test1_parse))
    assert_equals(('Lapras', 72), hw2_pandas.max_level(test1_pandas))
    # my own (test2)
    assert_equals(('Lapras', 72), hw2_manual.max_level(test2_parse))
    assert_equals(('Lapras', 72), hw2_pandas.max_level(test2_pandas))


def test_filter_range(test1_parse, test2_parse, test1_pandas, test2_pandas):
    """
    Tests the filter_range method
    """
    # given (test1)
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_manual.filter_range(test1_parse, 35, 72))
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_pandas.filter_range(test1_pandas, 35, 72))
    # my own (test2)
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_manual.filter_range(test2_parse, 35, 72))
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_pandas.filter_range(test2_pandas, 35, 72))


def test_mean_attack_for_type(test1_parse, test2_parse,
                              test1_pandas, test2_pandas):
    """
    Tests the mean_attack_for_type method
    """
    # given (test1)
    assert_equals(47.5,
                  hw2_manual.mean_attack_for_type(test1_parse, 'fire'))
    assert_equals(47.5,
                  hw2_pandas.mean_attack_for_type(test1_pandas, 'fire'))
    # my own (test2)
    assert_equals(47.5,
                  hw2_manual.mean_attack_for_type(test2_parse, 'fire'))
    assert_equals(47.5,
                  hw2_pandas.mean_attack_for_type(test2_pandas, 'fire'))


def test_count_types(test1_parse, test2_parse, test1_pandas, test2_pandas):
    """
    Tests the count_types method
    """
    # given (test1)
    assert_equals({'fire': 2, 'water': 2},
                  hw2_manual.count_types(test1_parse))
    assert_equals({'fire': 2, 'water': 2},
                  hw2_pandas.count_types(test1_pandas))
    # my own (test2)
    assert_equals({'fire': 2, 'water': 3},
                  hw2_manual.count_types(test2_parse))
    assert_equals({'fire': 2, 'water': 3},
                  hw2_pandas.count_types(test2_pandas))


def test_mean_attack_per_type(test1_parse, test2_parse,
                              test1_pandas, test2_pandas):
    """
    Tests the mean_attack_per_type method
    """
    # given (test1)
    assert_equals({'fire': 47.5, 'water': 140.5},
                  hw2_manual.mean_attack_per_type(test1_parse))
    assert_equals({'fire': 47.5, 'water': 140.5},
                  hw2_pandas.mean_attack_per_type(test1_pandas))
    # my own (test2)
    assert_equals({'fire': 47.5, 'water': 127},
                  hw2_manual.mean_attack_per_type(test2_parse))
    assert_equals({'fire': 47.5, 'water': 127},
                  hw2_pandas.mean_attack_per_type(test2_pandas))


def main():
    """
    main function
    """
    # Call your test functions here!
    test1 = '/home/pokemon_test.csv'
    test2 = '/home/pokemon_test2.csv'
    test1_parse = parse(test1)
    test2_parse = parse(test2)
    test1_pandas = pd.read_csv(test1)
    test2_pandas = pd.read_csv(test2)
    test_species_count(test1_parse, test2_parse, test1_pandas, test2_pandas)
    test_max_level(test1_parse, test2_parse, test1_pandas, test2_pandas)
    test_filter_range(test1_parse, test2_parse, test1_pandas, test2_pandas)
    test_mean_attack_for_type(test1_parse, test2_parse,
                              test1_pandas, test2_pandas)
    test_count_types(test1_parse, test2_parse, test1_pandas, test2_pandas)
    test_mean_attack_per_type(test1_parse, test2_parse,
                              test1_pandas, test2_pandas)


if __name__ == '__main__':
    main()
