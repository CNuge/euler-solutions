"""
By replacing the 1st digit of the 2-digit number *3, 
it turns out that six of the nine possible values: 
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, 
this 5-digit number is the first example having seven primes among the ten generated numbers, 
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
Consequently 56003, being the first member of this family, 
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
with the same digit, is part of an eight prime value family.

https://projecteuler.net/problem=51
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


def replacement_scan(number, prime_set):
	""" iteratively replace digits in a number and find a prime set equal to the length of the query""" 
	num_string = str(number)

	for i, x1 in enumerate(num_string):
		for j, x2 in enumerate(num_string):
			if i != j:
				prime_list = []
				for digit in range(0,10):
					new_num = list(num_string)
					new_num[i] = str(digit)
					new_num[j]= str(digit)

					new_int = int(''.join(new_num))
					if is_prime(new_int):

						prime_list.append(new_int)

				#below we use set, because the scan will record the initial number t
				if len(prime_list)== prime_set:
					return True, sorted(prime_list)
	return False, 0





if __name__ == '__main__':

replacement_scan(13, 6)

replacement_scan(56003, 7)

for i in range(56993, 1000000, 2):
	if is_prime(i):
		output = replacement_scan(i, 8)
		if output[0] == True:
			print(output[0])
			break














