# https://www.codewars.com/kata/54d512e62a5e54c96200019e/solutions/python

# Given a positive number n > 1 find the prime factor decomposition of n. 
# The result will be a string with the following form :

#  "(p1**n1)(p2**n2)...(pk**nk)"

# where a ** b means a to the power of b

# with the p(i) in increasing order and n(i) empty if n(i) is 1.

# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

def prime_factors(n):
    n_temp = n
    list_of_factors = []
    while n_temp != 1:
        return_list = factor_search(n_temp)
        list_of_factors.append(return_list[0])
        n_temp = return_list[1]
    output_string = ""
    for i in range(2, list_of_factors[-1] + 1):
        counter = list_of_factors.count(i)
        if counter == 1:
            output_string += f"({i})"
        elif counter > 1:
            output_string += f"({i}**{counter})"
    return output_string


def factor_search(n):
    for factor in range(2, n + 1):
        if not n % factor:
            return factor, int(n/factor)
    return 1
