"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

https://projecteuler.net/problem=9
"""


def is_triangle(a,b,c):
	if (a**2 + b**2) == c**2:
		return True
	return False


def py_triplet(total):
	""" find the product of the pythagorean triplet of number passed in, 
		if appliciable. 
		Pythagorean triplet is a set of three natural numbers, a < b < c"""
	for a in range(1,total-1):
		for b in range(1,total-1):
			c = total - a - b
			if is_triangle(a,b,c):
				return ("triplet:", a, b, c, "product:", a*b*c)


py_triplet(1000)


