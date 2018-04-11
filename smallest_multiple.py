
"""
2520 is the smallest number that can be divided by each of the numbers from 
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?


https://projecteuler.net/problem=5
"""

#brute force solution
def smallest_multiple():
	i = 1
	denom = 20

	while True:
		if i % denom == 0:
			while denom > 0:
				if i % denom == 0:
					denom -= 1
				else:
					denom = 20
					i += 1
					break
			else:
				return i
		else:
			print(i)
			i += 1

smallest_multiple()