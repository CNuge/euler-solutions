"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.

https://projecteuler.net/problem=6

"""


def calc_sum_squares(numbers):
	"""1^2 + 2^2 + ... + 10^2 = 385"""
	return sum((x**2 for x in numbers))

def calc_squared_sum(numbers):
	"""(1 + 2 + ... + 10)^2 = 55^2 = 3025"""
	return sum(numbers) ** 2

def ss_difference(numbers):
	sum_squares = calc_sum_squares(numbers)

	squared_sum = calc_squared_sum(numbers)

	return squared_sum - sum_squares


ss_difference(range(101))