"""
An irrational decimal fraction is created by concatenating the positive integers:

0.12345678910{1}112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


https://projecteuler.net/problem=40

"""


def build_num_string(maximum):
	dec_string = ''
	counter = 1
	while len(dec_string) < maximum:
		dec_string += str(counter)
		counter +=1
	return dec_string

if __name__ == '__main__':

	digits = []

	top_digit = 1000000

	decimals = build_num_string(top_digit)

	product = 1
	current = 1
	while current <= top_digit:
		product = product * int(decimals[current-1])
		current = current * 10

	print(product)