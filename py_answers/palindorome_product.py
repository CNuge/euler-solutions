"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of 
two 3-digit numbers.

https://projecteuler.net/problem=4

"""

def is_palindrome(input):
	if str(input) == str(input)[::-1]:
		return True

def palindrome_product():
	max_product = 0

	for x in range(999, 99, -1):
		for y in range(999, 99, -1):
			if is_palindrome(x*y):
				if x*y > max_product:
					max_product = x*y

	return max_product


palindrome_product()
