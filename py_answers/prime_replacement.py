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
from sympy import sieve
from sympy.ntheory.primetest import isprime
from itertools import permutations

def number_replacement(combo, digit_dict, prime_set):
    prime_list = []
    not_prime = 0

    for digit in range(0,10):
    	
    	test_dict = dict(digit_dict)
    	for pos in combo:
    		test_dict[pos] = digit
		new_dig = int(''.join([str(x) for x in test_dict.values()]))
		
		#make sure the number hasn't been shortened by a leading zero
		if len(str(new_dig)) == len(digit_dict.keys()):
			if isprime(new_dig):
				prime_list.append(new_dig)
			else:
				not_prime += 1
				if not_prime > (10 - prime_set):
					return []
	return prime_list


def replacement_scan(number, prime_set):
	""" replace components of the number, to check for prime permutations"""
	#want to isolate just the duplicates
	if len(set(str(number))) == len(str(number)):
		return False, []

	digit_dict = {k: int(v) for k, v in enumerate(str(number))}

	count_dig = {k : list(digit_dict.values()).count(k) for k in digit_dict.values() }

	combos = []
	for k, v in count_dig.items():
		if v > 1:
			combo = []
			for i, num in digit_dict.items():
				if num == k  :	
					combo.append(i)
			combos.append(combo)	
    	
	for combo in combos:
		prime_list = number_replacement(combo, digit_dict, prime_set)
		
	    out_list = list(set(prime_list))
		
		#below we use set, because the scan will record the initial number t
		if len(prime_list) == prime_set:
			return True, sorted(prime_list)
	return False, []



if __name__ == '__main__':


	prime_list = list(sieve.primerange(1, 10**6))

	replacement_scan(56003, 7 )
	replacement_scan(56773, 7 )


	ans = 0
	for i in prime_list:
		output = replacement_scan(i, 8)
		print(i)
		if output[0] == True:
			print(output[1])
			ans = output[1][0]
			break

	print(ans)








