"""
Avery Lee
CSE 163 AB
This program implements the functions for HW1 (Primer).
"""


def total(n):
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def count_divisible_digits(n, m):
    """
    parameters: integers n, m
    returns the number of digits in n that are divisible by m
    edgecase: when m=0, return 0 since you cannot divide by 0
    """
    if m == 0:
        return 0
    elif n == 0:
        return 1
    else:
        count_divisible = 0
        n = abs(n)
        while n > 0:
            digit = n % 10  # get the last digit
            if digit % m == 0:
                count_divisible += 1
            n //= 10  # remove the last digit
        return count_divisible


def is_relatively_prime(n, m):
    """
    parameters: integers n, m
    returns True or False depending on relatively prime to each other
    (don't have common factors besides 1)
    edgecase: 1 is relatively prime with all numbers
    """
    if (n == 1) or (m == 1):  # save some time
        return True
    factor = 2  # everything is divisible by 1 so start from 2
    iteration = 0
    # will return False and end while loop if not relatively prime
    while iteration <= min(n, m):
        if (n % factor == 0) and (m % factor == 0):  # not relatively prime
            return False
        factor += 1
        iteration += 1
    return True


def travel(directions, x, y):
    """
    parameters: string location directions, int x and y
    returns tuple that indicates a new position
    directions are uppercase or lowercase N, E, S, or W.
    all non-NESW characters are ignored.
    """
    directions = directions.upper()  # n, e, s, or w are also valid inputs
    location_list = [x, y]  # initial location
    for i in directions:
        if i == 'N':
            location_list[1] += 1
        elif i == 'E':
            location_list[0] += 1
        elif i == 'S':
            location_list[1] -= 1
        elif i == 'W':
            location_list[0] -= 1
        # all non NESW are ignored
    return tuple(location_list)


def compress(s):
    """
    parameters: string s
    returns string with each input character followed by its duplicative count
    example: aaabbb -> a3b3
    edgecase: empty strings return ''
    """
    if s == '':
        return ''
    else:
        new = ''
        only_chars = [s[0]]  # first character in s
        only_counts = [0]  # start with count 0
        for index, letter in enumerate(s):
            if letter != only_chars[-1]:  # not duplicate
                only_chars.append(letter)
                only_counts.append(1)
            else:  # immediate duplicate
                only_counts[-1] += 1
        for chars, counts in zip(only_chars, only_counts):
            new += (chars + str(counts))
        return new


def longest_word(file_name):
    """
    parameters: file_name string
    returns the longest word and its line number
    edgecase: empty files/no words return None, if tied return first occurrence
    """
    with open(file_name) as f:
        lines = f.readlines()
        if len(lines) <= 0:  # empty file
            return None
        else:
            longest = ''
            index = 1
            longest_index = 0
            for line in lines:
                line = line.split()  # into each token
                for word in line:
                    if len(word) > len(longest):
                        longest = word
                        longest_index = index
                index += 1

            return (str(longest_index) + ": " + longest)


def get_average_in_range(integers, low, high):
    """
    parameters: list of integers, integers low and high
    returns the average of numbers in the integers list between low and high
    edgecase: if no values in range return 0
    """
    total = 0
    count = 0
    for i in integers:
        if i >= low and i < high:
            count += 1
            total += i
    if count == 0:
        return 0
    else:
        return total / count


def mode_digit(n):
    """
    parameters: integer n
    returns the digit that appears most frequently
    edgecase: if tied return the bigger digit
    """
    n = abs(n)
    if n == 0:
        return 0
    else:
        nums = list(range(10))
        counts = {key: 0 for key in nums}  # dictionary of key of 0 to 9
        while n > 0:
            digit = n % 10  # digit at the end
            counts[digit] += 1
            n //= 10  # remove digit at the end
        mode = 0
        largest_count = 0
        for k, v in counts.items():
            if v >= largest_count:  # do = too to get the greatest k
                largest_count = v
                mode = k
        return mode
