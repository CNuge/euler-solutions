"""

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
is unusual in two ways: (i) each of the three terms are prime, 
and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?


https://projecteuler.net/problem=49
"""

from itertools import permutations

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


def eq_distance(list_of_numbers):
	""" take a list of 3+ numbers and determine if there is a set of three numbers
		int the list that have equal differences """

	#return the list of three numbers if they exist, return False otherwise

#iterate through numbers
def find_eq_prime_perms(prime_list):
	for x in range(1000, 10000):
		#get the permutations
		perms = [''.join(p) for p in permutations(str(x))]
		#isolate the prime ones
		prime_perms = [int(x) for x in list(set(perms)) if int(x) in prime_list]

		gap_check = eq_distance(prime_perms)
		if gap_check != False :
			return gap_check

	return False

if __name__ == '__main__':
	#need to have permutations that are prime and that have equal differences between them
	prime_list = []
	for x in range(1000, 10000):
		if is_prime(x):
			prime_list.append(x)

	numbers = find_eq_prime_perms(prime_list)

	print(''.join(numbers))
