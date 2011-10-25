num1 = 1
num2 = 1
sum = 0

while num2 < 4000000:
	temp = num2
	num2 = num1 + num2
	num1 = temp
	if num2 % 2 == 0:
		sum += num2

print sum

