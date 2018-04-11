"""
https://projecteuler.net/problem=1


If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_3_5_multiples(max):
	""" iterate through the integers lower than the max value
		add them to the total if they are evenly divisible by 3 or 5 """
	total = 0
	for i in range(max):
		if i % 5 == 0 or i % 3 == 0 :
			total += i
	return total


ans = sum_3_5_multiples(1000)
ans

#correct ans given