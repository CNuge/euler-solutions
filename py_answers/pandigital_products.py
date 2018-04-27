"""
We shall say that an n-digit number is pandigital if it makes use of 
all the digits 1 to n exactly once; for example, 
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.

https://projecteuler.net/problem=32
"""


def pandigit_set(*args):
	string_args = [str(x) for x in args]
	dig_string = ''.join(string_args)
	unique_digs = set(dig_string)
	if '0' in unique_digs:
		return False
	if len(unique_digs) == 9:
		pan_digits = ''.join([str(x) for x in range(1,10)])
		if unique_digs == set(pan_digits):
			return True
	return False


def pandigital_product(number):
	for x in range(1, int(number/2)+1):
		if number%x == 0:
			if pandigit_set(number, x, int(number/x)) == True:
				print(number, x, int(number/x))
				return True
	return False


if __name__ == '__main__':

	pandigit_product_sum = 0

	for i in range(10000):
		if pandigital_product(i) == True:
			pandigit_product_sum += i
			print(f'sum = {pandigit_product_sum}')
