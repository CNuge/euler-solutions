"""
The decimal number, 585 = 10010010012 (binary), 
is palindromic in both bases.

Find the sum of all numbers, less than one million, 
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, 
may not include leading zeros.)

https://projecteuler.net/problem=36
"""


def is_palindrome(input):
	if str(input) == str(input)[::-1]:
		return True


def bin_string(number):
	""" take a number and return a string representation of its binary value """

	return bin(number)[2:]


if __name__ == '__main__':

	total = 0

	for i in range(0,1000000):
		if is_palindrome(i) and is_palindrome(bin_string(i)):
			total += i

	print(total)
