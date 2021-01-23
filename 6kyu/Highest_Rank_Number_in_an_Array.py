# https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python

# Complete the method which returns the number which is most frequent in 
# the given input array. If there is a tie for most frequent number, 
# return the largest number among them.

# Note: no empty arrays will be given.
# Examples

# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

def highest_rank(arr: list):
    list_of_number = []
    for number in arr:
        if number not in list_of_number:
            list_of_number.append(number)
    frequent = 0
    winner = None
    for number in list_of_number:
        count = arr.count(number)
        if count > frequent:
            winner = number
            frequent = count
        elif count == frequent:
            winner = max([number, winner])
    return winner

# test.describe("Example Tests")
# test.it("Example Test Case")
# test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
# test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10)