"""The following iterative sequence is defined for the set of positive integers:

    n  n/2 (n is even)
    n  3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13  40  20  10  5  16  8  4  2  1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
"""


winner = None
max_count = 0

class Cache(object):

    def find_count(self, n):
        count = 1
        original_n = n

        while n != 1:
            if self.get_count(n):
                count += self.get_count(n)
                break

            if n % 2 == 0:
                n = n/2
            else:
                n = 3*n + 1

            count += 1

        setattr(self, '_%s' % original_n, count)

    def get_count(self, n):
        try:
            return getattr(self, '_%s' % n)
        except AttributeError:
            return None

cache = Cache()

for n in xrange(1, 1000000, 2):
    cache.find_count(n)

    if cache.get_count(n) > max_count:
        winner = n
        max_count = cache.get_count(n)

print winner
