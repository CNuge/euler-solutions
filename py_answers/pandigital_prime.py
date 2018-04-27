"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
 For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?


https://projecteuler.net/problem=41
"""


from itertools import permutations


def is_prime(number):
	""" take a number and return a boolean indicating
		if the number is prime or not """
	if number < 0:
		return False
	if number < 4:
		return True
	#start with number 2, iterate up until up to half the number is reached
	for x in range(2, int(number/2)+1):
		if number%x == 0:
			return False
	return True


def digit_permutations(number):
	str_dig = list(str(number))	
	return [int(''.join(x)) for x in permutations(str_dig)]


def pandigit_prime():
	max_pan_prime = 0

	digits = '987654321'

	for i in range(0, len(digits)-1):
		dig_sub = digits[i:]
		perms = digit_permutations(int(dig_sub))
		for perm in perms:
			print(perm)
			if is_prime(perm):
				if perm > max_pan_prime:
					return perm # based on the direction of the permutations, 
								# we can stop at the first one we find since order == descending
			

if __name__ == '__main__':

	pandigit_prime()


