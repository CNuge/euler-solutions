"""
By listing the first six prime numbers: 
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

https://projecteuler.net/problem=7

"""

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



def prime_ten_thousand_and_one():
	"""euler says 1 isn't prime... so list from 2 onwards"""
	prime_count = 0

	number = 1 #start at 2 as the first in the list... apparently 1 doesn't count"""

	while prime_count < 10001:
		number += 1
		if is_prime(number) == True:
			prime_count += 1		
		
	return (number, prime_count)
