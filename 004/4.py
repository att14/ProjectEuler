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
	
