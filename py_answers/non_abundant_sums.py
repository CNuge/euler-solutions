"""
A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be
 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than 
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater 
than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even 
though it is known that the greatest number that cannot be 
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the 
sum of two abundant numbers.

https://projecteuler.net/problem=23

"""
import math

def divisors(number):
	""" take a number and determine its integer divisors """
	divisor_list = [1]
	for div1 in range(2, int(math.sqrt(number)+1)):
		if number % div1 == 0:
			divisor_list.append(div1)
			div2 = int(number / div1)
			if div1 != div2:
				divisor_list.append(div2)

	return divisor_list

def divisorsb(number):
	""" take a number and determine its integer divisors """
	divisor_list = [1]
	for div1 in range(2, int((number/2)+1)):
		if number % div1 == 0:
			divisor_list.append(div1)
	return divisor_list





def is_abundant(number):
	""" take an input number and see if its divisors sum 
		to more than the number. True if abundant"""
	sum_divisors = 0
	div_list = divisors(number)
	
	for x in div_list:
		sum_divisors += x
	
	if number < sum_divisors:
		return True

	return False


def two_abundant(number):
	""" split into two parts 1 -> number*.5 
		See if two abundant numbers sum to the original.
		If not, return false, if there are two abundants that sum to the number,
		then return true. """
	for test1 in range(2,int(number/2)+1):
		test2 = number - test1
		if test2 < 1:
			test2 = 1

		if is_abundant(test1) and is_abundant(test2):
			return True

	return False

def sum_non_abundant_sums():
	total = 0
	abundant_max = 28123

	for x in range(1, abundant_max+1):
		if two_abundant(x) == False:
			total += x

	return total


if __name__ == "__main__":


	sum_non_abundant_sums()

