"""
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. 
The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. 
However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, 
for which their sum and difference are pentagonal 
and D = |Pk − Pj| is minimised; what is the value of D?


https://projecteuler.net/problem=44

"""


#build a list of pentagonal numbers


def pentagonal_numbers(max):
	pentagonal_nums = []
	for n in range(1, max):
		pent = (n * ((3*n) - 1)) / 2
		pentagonal_nums.append(int(pent))
	return pentagonal_nums

def first_pent_pair(pent_list):
	for i, n1 in enumerate(pent_list):
		for n2 in pent_list[:i]:
			if n1 + n2 in pent_list[i:]:
				if n1 - n2 in pent_list[:i]:
					return n1,n2

if __name__ == '__main__':

	pent_pairs = []

	pent_list = pentagonal_numbers(10000)

	first_encountered = first_pent_pair(pent_list)
	print(first_encountered[0]- first_encountered[1])
	#(7042750, 1560090)


