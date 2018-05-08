"""
A googol (10^100) is a massive number: 
one followed by one-hundred zeros; 
100^100 is almost unimaginably large: 
one followed by two-hundred zeros. 

Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form,

a^b, where a, b < 100, what is the maximum digital sum?


https://projecteuler.net/problem=56
"""


def power_digit_sum(a, b):
	data = a ** b
	total = 0

	for i in str(data):
		total += int(i)

	return total


if __name__ == '__main__':

	maximal_sum = 0

	for a in range(1,100):
		for b in range(1,100):
			power_sum = power_digit_sum(a, b)

			if power_sum > maximal_sum:
				maximal_sum = power_sum

	print(maximal_sum)