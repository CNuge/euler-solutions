"""
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive 
integer values 0≤n≤39. However, when 

n=40,402+40+41=40(40+1)+41 

is divisible by 41, 
and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 
80 primes for the consecutive values 0≤n≤79. 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, 
a and b, for the quadratic expression that produces the maximum number of primes 
for consecutive values of n, starting with n=0.

https://projecteuler.net/problem=27
"""

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


def prime_string(a,b):	
	n = 0
	prime_len = 0
	while True:
		val = (n**2) + (a*n) + b
		if is_prime(val) == True:
			prime_len += 1
			n +=1
		else:
			return prime_len

if __name__ == '__main__':
	max_list = (0, 0, 0)

	for a in range(-1000, 1001):
		for b in range(-1000, 1001):
			len_of_pattern = prime_string(a,b)
			if len_of_pattern > max_list[0]:
				max_list = (len_of_pattern, a, b)

	print(max_list)
	print(max_list[1] * max_list[2])




