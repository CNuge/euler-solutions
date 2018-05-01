"""
If p is the perimeter of a right angle triangle with integral length sides, 

{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?


https://projecteuler.net/problem=39

"""


def is_right_tri(a,b,c):
	if (a ** 2) + (b ** 2) == (c ** 2):
		return True
	return False


def count_triangles(perimeter):
	print(perimeter)
	right_tri_count = 0

	for a in range(0, perimeter/2):
		for b in range(0, perimeter/2):
			c = perimeter - a - b
			if c > a and c > b:
				if is_right_tri(a,b,c) == True:
					right_tri_count += 1
	return right_tri_count


if __name__ == '__main__':

	max_perim = 0
	max_tri_count = 0

	for i in range(3, 1001):
		tri_count = count_triangles(i)
		if tri_count > max_tri_count:
			max_tri_count = tri_count
			max_perim = i

	print(f'the optimized perimeter is: {max_perim}')
	print(f'which produces {max_tri_count} integral triangles')


