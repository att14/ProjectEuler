"""A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for a in range(1, 500):
    for b in range(1, 500):
        c = (a**2 + b**2)**0.5
        if a + b + c != 1000:
            continue
        else:
            print int(a * b * c)
            exit()

