"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def isprime(n):
    n = abs(int(n))
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5+1), 2):
        if n % x == 0:
            return False
    return True

n = 600851475143

for x in range(3, int(n**0.5+1), 2):
    if n % x == 0:
        if isprime(x) is True:
            print x

