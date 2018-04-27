"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by
 1, 2, 3, 4, and 5, giving the pandigital, 
918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 
9-digit number that can be formed as the concatenated 
product of an integer with (1,2, ... , n) where n > 1?


https://projecteuler.net/problem=38
"""


def pandigit_string(dig_string):
	if len(dig_string) != 9:
		return False
	unique_digs = set(dig_string)
	if '0' in unique_digs:
		return False
	if len(unique_digs) == 9:
		pan_digits = ''.join([str(x) for x in range(1,10)])
		if unique_digs == set(pan_digits):
			return True
	return False


def pan_digit_product(num):
	total = ''
	mul = 1
	while len(total) < 10 or total == '':
		if len(set(total)) != len(total):
			return 0
		val = num * mul
		total += str(val)
		mul += 1
		if pandigit_string(total) == True:
			return int(total)
	return 0


if __name__ == '__main__':

	largest = 0
	for x in range(0,10000):
		product_set = pan_digit_product(x)
		if product_set != 0:
			if product_set > largest:
				largest = product_set

	print(largest)


print(largest)
