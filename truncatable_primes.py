"""
The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly 
we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable 
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


https://projecteuler.net/problem=37

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


def truncate_right(number):
	str_num = str(number)
	while len(str_num) > 0:
		if str_num == '1': #1 is not prime... I always forget this :l
			return False
		if is_prime(int(str_num)) == False:
			return False
		str_num = str_num[:-1]
	return True

def truncate_left(number):
	str_num = str(number)
	while len(str_num) > 0:
		if str_num == '1':
			return False
		if is_prime(int(str_num)) == False:
			return False
		str_num = str_num[1:]
	return True




if __name__ == '__main__':

	truncate_right(3797)

	truncate_left(3797)

	number = 11

	trunc_total = 0
	trunc_found = 0

	while trunc_found < 11:
		if is_prime(number) == True:
			if truncate_right(number) == True and truncate_left(number) == True:
				trunc_total += number
				trunc_found += 1
				print(number)
		number =  number + 2

	print(f'The search found {trunc_found} both sided truncatable primes')
	print(f'Their total is: {trunc_total}')




