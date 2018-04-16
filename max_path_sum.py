"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying 
every route. However, Problem 67, is the same challenge with a triangle containing 
one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)


https://projecteuler.net/problem=18

https://projecteuler.net/problem=67

curl https://projecteuler.net/project/resources/p067_triangle.txt > big_triangle.txt

"""


def sum_traverse_triangle(triangle):
	
	for rev_i, row in enumerate(triangle[::-1]):
		if rev_i == 0:
			continue
		i = len(triangle) - 1 - rev_i

		for j, pos in enumerate(row):
			below = triangle[i+1][j]
			below_right =  triangle[i+1][j+1]
			if below > below_right:
				triangle[i][j] = pos + below
			elif below_right >= below :
				triangle[i][j] = pos + below_right
	return triangle


def read_triangle(filename):
	triangle = []
	with open(filename) as file:
		for i, line in enumerate(file):
			triangle.append([int(x) for x in line.split()])

	return triangle


if __name__ == '__main__':

	lil_file = 'little_triangle.txt'
	lil_triangle = read_triangle(lil_file)

	little_ans = sum_traverse_triangle(lil_triangle)

	print(little_ans[0][0])


	big_file = 'big_triangle.txt'

	big_triangle = read_triangle(big_file)
		
	big_ans = sum_traverse_triangle(big_triangle)

	print(big_ans[0][0])


	outstring = ''
	for line in big_triangle:
		line_string = '\t'.join([str(x) for x in line])
		outstring += line_string + '\n'

	output = 'test.txt'
	file = open(output, 'w')
	file.write(outstring)
	file.close()








