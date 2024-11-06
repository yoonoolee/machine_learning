"""
Avery Lee
CSE 163 AB
This program implements the functions for HW2 with pandas.
HW2 reads in a csv file of pokemon data and provides analysis
such as the count, maximum, and mean of different attributes.
"""


import pandas as pd


def species_count(data):
    """
    parameter: dataframe of pokemon info
    returns the count of unique species
    """
    species = data['name'].unique()
    return len(species)


def max_level(data):
    """
    parameter: dataframe of pokemon info
    returns a tuple (name, level) of the pokemon with the highest level
    special case: if tied, returns the one that appears first
    """
    highest = data['level'].idxmax()  # get index of the highest level
    highest_name = data.loc[highest, 'name']
    highest_level = data.loc[highest, 'level']
    return (highest_name, highest_level)


def filter_range(data, lower, upper):
    """
    parameter: dataframe of pokemon info, lower and upper bounds
    returns a list of pokemon names whose levels are within bounds
    """
    within_bounds = data[(data['level'] >= lower) & (data['level'] < upper)]
    within_bounds = list(within_bounds['name'])
    return within_bounds


def mean_attack_for_type(data, tp):
    """
    parameter: dataframe of pokemon info, type (tp)
    returns the average of atk of the given type
    special case: if no pokemon of given type, return None
    """
    if tp not in list(data['type']):  # check if type exists
        return None
    else:
        avg = float((data[data['type'] == tp])['atk'].mean())
        return avg


def count_types(data):
    """
    parameter: dataframe of pokemon info
    returns a dictionary of the count (value) of each type (key)
    """
    return dict(data.groupby('type')['type'].count())


def mean_attack_per_type(data):
    """
    parameter: dataframe of pokemon info
    returns a dictionary of the average atk (value) for each type (key)
    """
    return dict(data.groupby('type')['atk'].mean())


def main():
    """
    main function
    """
    data = pd.read_csv('/home/pokemon_box.csv')

    print('Number of species:', species_count(data))
    print('Highest level pokemon:', max_level(data))
    print('Low-level Pokemon:',  filter_range(data, 1, 9))
    print('Average attack for fire types:',
          mean_attack_for_type(data, 'fire'))
    print('Count of each Pokemon type:')
    print(count_types(data))
    print('Average attack for each Pokemon type:')
    print(mean_attack_per_type(data))


if __name__ == '__main__':
    main()
