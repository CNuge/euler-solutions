"""
The series, 1^1 + 2^2 + 3^3 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


https://projecteuler.net/problem=48

"""

total = 0

for x in range(1, 1001):
	y = x ** x
	total += y

print(str(total)[-10:])