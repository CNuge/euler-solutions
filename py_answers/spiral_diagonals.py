"""
Starting with the number 1 and moving to the right in a clockwise direction 
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?

https://projecteuler.net/problem=28
"""

def spiral_addition(size):
	num_list = [x for x in range(1,(size*size)+1)][::-1]
	total = 0
	times = 0
	increment = size-1
	pos = 0

	while pos < len(num_list) and increment > 0:
		#add current position
		print(num_list[pos])
		total += num_list[pos]
		#increment
		if times == 4:
			times = 1
			increment -= 2
			pos += increment
		else:
			times += 1
			pos += increment
	return total

spiral_addition(5) # 101
spiral_addition(6) # 170
spiral_addition(7) # 260



spiral_addition(1001)



