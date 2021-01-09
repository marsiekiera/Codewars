# https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python

# Count the number of divisors of a positive integer n

def divisors(n):
    count = 0
    for i in range(1, n + 1):
        if not n % i:
            count += 1
    return count
