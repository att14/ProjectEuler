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

sum = 2

for x in range(3, 2000000, 2):
	if isprime(x) is True:
		sum += x

print sum

