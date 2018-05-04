"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

https://projecteuler.net/problem=50

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
	


def list_primes(max_val):
	""" return a list of primes under a maximal value """
	prime_list = [2]
	for x in range(3, max_val, 2):
		if is_prime(x):
			prime_list.append(x)
	
	return prime_list


def max_len_prime_sum(index, prime_list, top_value):
	
	#keep track of the largest prime string sum seen
	max_val = 0
	max_prime_len = 0
	#the total
	val = prime_list[index]
	length = 1

	#iterate through the primes
	for num in prime_list[index+1:]:
		#make a new value by adding the next prime to the total
		new_val = val + num
		#if the new value exceeds the cap, return the longest string product seen
		if new_val > top_value:
			return max_val, max_prime_len		
		
		length += 1

		# make the current value equal to the addition of the 
		val = new_val
		# if the value is in the prime list it is the largest prime product seen
		if is_prime(val):
			max_prime_len = length
			max_val = val

	return max_val, max_prime_len

	
larger_prime_list = list_primes(1000)


for i , num in enumerate(larger_prime_list):
	consecutive_sum, length_sum = max_len_prime_sum(i, larger_prime_list, 1000)
	print(i, consecutive_sum, length_sum)


print(max_value)
print(max_len)

if __name__ == '__main__':


prime_list = list_primes(10000)

len(prime_list)

max_len = 0
max_value = 0

for i, number in enumerate(prime_list):
	consecutive_sum, length_sum = max_len_prime_sum(i, prime_list, 1000000)
	if length_sum > max_len:
		print(i, consecutive_sum, length_sum)
		max_len = length_sum
		max_value = consecutive_sum

print(max_value)
print(max_len)

# we know it will be a long list of primes, as the number for under 1000 had 21 terms 








