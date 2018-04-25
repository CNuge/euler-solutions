"""
In England the currency is made up of pound, £, and pence, p, 
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?


https://projecteuler.net/problem=31
"""


def make_change():
	""" build it from the bottom up
		figure out the number of ways possible to make 1 pence (only one) 
		then whe"""
	target = 200

	vals = [1, 2, 5, 10, 20, 50, 100, 200] #all the pence values

	ways = [1] + [0]*target	#single way to make 1, then 0s to sum to each penny on the way to 2 pounds

	for val in vals: #for each value
		for i in range(val, len(ways)): #iterate from it up to the maximum
			ways[i] += ways[i-val] # adding the number of ways to reach x minus the current value to the current cell
	#once that is completed, we have summed all the ways to get to the maximu		
	return ways[target] #then just return the final value in the list


def brue_make_change_methods():
	change_ways = 0

	for two in range(0,2):
		for one in range(0,3):
			for fifty in range(0,5):
				for twenty in range(0,11):
					for ten in range(0,21):
						for five in range(0,41):
							for twop in range(0,101):
								for onep in range(0,201):
									total= (two*2) + \
											(one * 1) + \
											(fifty *.5) + \
											(twenty * .2) + \
											(ten * .1) + \
											(five * .05) + \
											(twop * .02) + \
											(onep * 0.01)
									total_change = format(total, '.2f')
									print(total_change)
									if total_change == 2.00:
										print(f'change:{change_ways}')
										change_ways += 1
	return change_ways


if __name__ == '__main__':
	make_change()

	#SLOOOOOOOW
	#brue_make_change_methods()



