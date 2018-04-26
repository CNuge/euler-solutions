"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
 which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, 
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its 
lowest common terms, find the value of the denominator.

https://projecteuler.net/problem=33
"""


def digit_cancel_check(components):
	""" try to cancel the digits of a fraction in a non trivial manner,
		if possible the return True and the num and denom numbers """

	if components[0] == components[2] and components[1] == components[3]:
		return False, 1, 1

	if components[1] == 0 and components[3] == 0:
		return False, 1, 1

	full_num = int(str(components[0])+str(components[1]))
	full_denom = int(str(components[2])+str(components[3]))
	if full_num > full_denom:
		return False, 1, 1
	try: 
		if components[0] == components[2]:
			sub_num = components[1] 
			sub_denom = components[3]
			if  full_num/full_denom == sub_num/sub_denom:
				return True, full_num, full_denom

		if components[0] == components[3]:
			sub_num = components[1] 
			sub_denom = components[2]
			if  full_num/full_denom == sub_num/sub_denom:
				return True, full_num, full_denom

		if components[1] == components[2]:
			sub_num = components[0] 
			sub_denom = components[3]
			if  full_num/full_denom == sub_num/sub_denom:
				return True, full_num, full_denom

		if components[1] == components[3]:
			sub_num = components[0] 
			sub_denom = components[2]
			if  full_num/full_denom == sub_num/sub_denom:
				return True, full_num, full_denom
		return False, 1, 1
	except:
		return False, 1, 1



if __name__ == '__main__':

	component_list = []

	for t_1 in range(1,10):
		for t_2 in range(0,10):
			for b_1 in range(1,10):
				for b_2 in range(0,10):
					component_list.append((t_1,t_2,b_1,b_2))

	cancel_fractions = []
	for dig_set in component_list:
		data = digit_cancel_check(dig_set)
		if data[0] == True:
			cancel_fractions.append(data[1:])

	len(cancel_fractions)
	cancel_fractions

	prod_num = 1
	prod_denom = 1

	for i in cancel_fractions:
		prod_num = prod_num * i[0]
		prod_denom = prod_denom * i[1]

	prod_num/prod_denom
