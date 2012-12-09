"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def ispal(n):
    s = str(n)
    l = len(s)
    for x in range(0, l):
        if s[x] != s[l - x - 1]:
            return False
    return True

for x in reversed(range(900, 999)):
    for y in reversed(range(900, 999)):
        if ispal(x * y):
            print x * y
