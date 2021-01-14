# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    list_of_odd = []
    for number in seq:
        if number not in list_of_odd:
            list_of_odd.append(number)
        else:
            list_of_odd.remove(number)
    if len(list_of_odd) != 1:
        return None
    else:
        return list_of_odd[0]
