"""
Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""
import numpy as np

def read_data(infile):
	data = []
	with open(infile) as file:
		for line in file:
			x = line.rstrip().split(',')
			base = int(x[0])
			exp = int(x[1])
			data.append((base,exp))
	return data



def get_top_val(exp_data):
	mod = 7
	top_pos = 0
	top_val = 0

	for pos, pair in enumerate(exp_data):

		#nned to look up how to use these to compare large primes
		pow_val = pow(pair[0], pair[1], mod)






"""
	bases = np.array([x[0] for x in exp_data])
	exps = np.array([x[1] for x in exp_data])

	values = np.power(bases, exps)
"""




if __name__ == '__main__':
	#read in the data
	data = read_data('base_exp.txt')




examples = [
(519432,525806),
(632382,518061),
(78864,613712),
]
