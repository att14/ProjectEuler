sumSq = 0
sqSum = 0

for x in range(1, 101):
	sumSq += x**2

for x in range(1, 101):
	sqSum += x

sqSum = sqSum**2

diff = sqSum - sumSq
print diff

