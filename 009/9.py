for a in range(1, 500):
	for b in range(1, 500):
		c = (a**2 + b**2)**0.5
		if a + b + c != 1000:
			continue
		else:
			print int(a * b * c)
			exit()

