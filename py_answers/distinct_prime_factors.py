"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?

https://projecteuler.net/problem=47
"""
from math import sqrt

def is_prime(number):
	""" take a number and return a boolean indicating
		if the number is prime or not """
	if number < 4:
		return True
	#start with number 2, iterate up until up to half the number is reached
	for x in range(2, int(number/2)+1):
		if number%x == 0:
			return False
	return True


def list_factors(number):
	factors = []

	for i in range(2,int(sqrt(number)+1)):
		if number % i == 0:
			factors.append(i)
			factors.append(int(number/i))

	return factors

def prime_count(num_list):
	count = 0
	for x in num_list:
		if is_prime(x):
			count += 1
	return count


if __name__ == '__main__':

	streak = 0
	number = 0
	while streak < 4:
		number += 1
		factors = list_factors(number)
		no_dup_factors = list(set(factors))

		if prime_count(no_dup_factors) >= 4:
			streak += 1
		else:
			streak = 0
	else:
		print([x for x in range(number-3, number+1)])

	"""
	list_factors(14)
	list_factors(15)


	list_factors(644)
	list_factors(645)
	list_factors(646)
	"""