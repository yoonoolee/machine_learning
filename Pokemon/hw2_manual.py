"""
Avery Lee
CSE 163 AB
This program implements the functions for HW2 without pandas.
HW2 reads in a csv file of pokemon data and provides analysis
such as the count, maximum, and mean of different attributes.
"""


def species_count(data):
    """
    parameter: list of dictionaries of pokemon info
    returns the count of unique species
    """
    species_unique = set()
    for dictionary in data:
        species_unique.add(dictionary['name'])  # only add the unique names
    return len(species_unique)


def max_level(data):
    """
    parameter: list of dictionaries of pokemon info
    returns a tuple (name, level) of the pokemon with the highest level
    special case: if tied, returns the one that appears first
    """
    highest_level = 0
    highest_name = ''
    for dictionary in data:
        # > instead of >= will ensure choosing first appearance
        if dictionary['level'] > highest_level:
            highest_level = dictionary['level']
            highest_name = dictionary['name']
    return (highest_name, highest_level)


def filter_range(data, lower, upper):
    """
    paramters: list of dictionaries of pokemon info, lower and upper bounds
    returns a list of pokemon names whose levels are within bounds
    """
    pokemon_in_bound = []
    for dictionary in data:
        if (dictionary['level'] >= lower) and (dictionary['level'] < upper):
            pokemon_in_bound.append(dictionary['name'])
    return pokemon_in_bound


def mean_attack_for_type(data, tp):
    """
    paramters: list of dictionaries of pokemon info, type (tp)
    returns the average of atk of the given type
    special case: if no pokemon of given type, return None
    """
    count = 0
    add = 0
    for dictionary in data:
        if dictionary['type'] == tp:
            add += dictionary['atk']
            count += 1
    if count == 0:  # no pokemon of given type
        return None
    else:
        return add / count


def count_types(data):
    """
    parameter: list of dictionaries of pokemon info
    returns a dictionary of the count (value) of each type (key)
    """
    counts = {}
    for dictionary in data:
        tp = dictionary['type']
        if tp not in counts:
            counts[tp] = 1
        else:
            counts[tp] += 1
    return counts


def mean_attack_per_type(data):
    """
    parameter: list of dictionaries of pokemon info
    returns a dictionary of the average atk (value) for each type (key)
    """
    total_attacks = {}
    count_attacks = {}
    for dictionary in data:
        tp = dictionary['type']
        if tp not in total_attacks:  # first initialization
            total_attacks[tp] = dictionary['atk']
            count_attacks[tp] = 1
        else:
            total_attacks[tp] += dictionary['atk']
            count_attacks[tp] += 1
    mean_attacks = {x: float(total_attacks[x])/count_attacks[x]
                    for x in total_attacks}

    return mean_attacks
