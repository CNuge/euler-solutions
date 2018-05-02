"""
The number, 1406357289, is a 0 to 9 pandigital number because it is 
made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.


https://projecteuler.net/problem=43
"""
from itertools import permutations


def pandigit_set(*args):

	string_args = [str(x) for x in args]
	dig_string = ''.join(string_args)
	unique_digs = set(dig_string)

	if len(dig_string) == 10:
		
		pan_digits = ''.join([str(x) for x in range(0,10)])
		if unique_digs == set(pan_digits):
			return True
	return False


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


def list_primes(length):

	number = 1
	prime_list = []

	while len(prime_list) < length:
		number += 1
		if is_prime(number) == True:
			prime_list.append(number)

	return prime_list	


def sliding_prime_check(number, list_of_primes):
	num_string = str(number)
	window = 1

	while window + 3 <= len(num_string):
		sub_num = int(num_string[window : window + 3])

		if sub_num % list_of_primes[window - 1] != 0:
			return False

		window += 1
	
	return True

if __name__ == '__main__':
"""problem doesn't state if leading zeros allowed, so I'm trying both below
	turns out no leading zeros!"""


prime_list = list_primes(10)

perms = [''.join(p) for p in permutations('0123456789')]

sum_pandigit_primes = 0

for p in perms:
	if sliding_prime_check(int(p), prime_list) == True:
		sum_pandigit_primes += int(p)

print(sum_pandigit_primes)

sum_pandigit_primes_no_zeros = 0

for p in perms:
	if p[0]!='0':
		if sliding_prime_check(int(p), prime_list) == True:
			sum_pandigit_primes_no_zeros += int(p)

print(sum_pandigit_primes_no_zeros)




test_num = 1406357289

sliding_prime_check(test_num, prime_list)



