"""
It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, 
x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

https://projecteuler.net/problem=52
"""


def permu_check(value, multiple):
	""" times a value by the given multiple, True if they contain the same digits """
	new_val = value * multiple

	val_components = sorted(list(str(value)))
	new_val_components = sorted(list(str(new_val)))

	if val_components == new_val_components :
		return True

	return False


def multiple_permu_check(value, max_multiple):
	for i in range(1, max_multiple+1):
		if permu_check(value, i) == False:
			return False
	return True



if __name__ == '__main__':
	found = False
	number = 0

	while found == False:
		number += 1
		if multiple_permu_check(number, 6) == True:
			found = True
	else:
		print(number)
