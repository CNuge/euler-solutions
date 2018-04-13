"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

https://projecteuler.net/problem=16

"""


def digit_sum(number):
	num_list = [x for x in str(number)]
	total = 0
	for x in num_list:
		total += int(x)
	return total


digit_sum(2**1000)