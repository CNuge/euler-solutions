"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

https://projecteuler.net/problem=76
"""


def count_summations(sum_to):

	sum_to
	vals = range(1, sum_to-1)

	ways = [1] + [0]*sum_to

	for val in vals: #for each value
		for i in range(val, len(ways)): #iterate from it up to the maximum
			ways[i] += ways[i-val]
	return (ways[sum_to])+1

if __name__ == '__main__':
	print(count_summations(100))