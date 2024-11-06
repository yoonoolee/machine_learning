"""
Avery Lee
CSE 163 AB
This program implements the functions for HW0
"""


def funky_sum(a, b, mix):
    """
    parameters: a and b (numbers), mix (ratio for b)
    returns a ratio of a and b based on the mix value (the ratio for b).
    if mix is 0 or less, result is same as a.
    if mix is 1 or more, result is same as b.
    """
    if mix <= 0:
        return a
    elif mix >= 1:
        return b
    else:
        return a * (1 - mix) + b * (mix)


def total(n):
    """
    parameters: n (number)
    returns the sum of 0 to n inclusive. if n is negative, return None value.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def swip_swap(source, c1, c2):
    """
    parameters: string source, characters c1, c2
    returns string source with characters c1 and c2 swapped
    """
    # required to use str concatenation with + operator for this problem
    temp = ""
    for i in source:
        if i == c1:
            temp += c2
        elif i == c2:
            temp += c1
        else:
            temp += i
    source = temp

    return source
