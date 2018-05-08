"""
It is possible to show that the square root of two can be expressed 
as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, 
but the eighth expansion, 1393/985, is the first example where the 
number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a 
numerator with more digits than denominator?


https://projecteuler.net/problem=57
"""

from fractions import Fraction


def find_last_2(formula):
	""" search the formula string and return the index position that contains the
		last '2' in the formual """
	for i , digit in enumerate(formula[::-1]):
		if digit == '2':
			return -(1+i)


def continued_fraction( formula ):
	"""take a string representing the sqrt(2) as a recurring fraction and
		provide the next occurance by replacing the trailing denominator"""

	new_denom = '(2 + 1/2)'

	last_2 = find_last_2(formula)

	new_formula = formula[:last_2] + new_denom + formula[last_2+1:]

	return new_formula



def iterate_sqrt_2(max_iter):
	count = 0

	iteration = 1
	formula = '1 + (1/2)'

	while iteration < max_iter :

		iteration += 1

		formula = continued_fraction(formula)
		value = eval(formula)

		vf = Fraction(value).limit_denominator(10000)

		if len(str(vf.numerator)) > len(str(vf.denominator)):
			count += 1

	return count


if __name__ == '__main__':

	eval('1 + 1/2')

	continued_fraction('1 + 1/(2 + 1/2)') == '1 + 1/(2 + 1/(2 + 1/2))'

	ans = iterate_sqrt_2(1000)

	print(ans)


	Fraction(41/29)


	Fraction(1.4).limit_denominator(10000)
