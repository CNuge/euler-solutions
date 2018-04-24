"""
The number, 197, is called a circular prime because all rotations of the digits: 

197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 

2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

https://projecteuler.net/problem=35

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

def rotate_string(input):
	""" take a string and move the first character to the end """
	return input[1:]+ input[0]

def circular_prime(number):
	""" take a number and rotate the digits, 
		checking at each iteration if the number is prime """
	if is_prime(number) == True:
		str_num = str(number)
		for x in range(1, len(str_num)):
			str_num = rotate_string(str_num)
			if is_prime(int(str_num)) == False:
				return False
		return True
	else:
		return False
	

if __name__ == '__main__':

	circle_prime_count = 1 #counting 2 so we can step by 2
	possible_components = set(['1','3','5','7','9']) #seems that the component digits need to be 1,3,5,7,9

	for x in range(3,1000000,2): #skip the even numbers
		digit_set = set(str(x))
		if digit_set.union(possible_components) != possible_components:
			continue
		if circular_prime(x) == True:
			circle_prime_count += 1

	print(circle_prime_count)