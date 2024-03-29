"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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

count = 1
num = 1

while count < 10001:
    num += 2
    if isprime(num) is True:
        count += 1

print num

