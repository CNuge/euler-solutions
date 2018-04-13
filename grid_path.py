"""
https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

This one has a picture go look at it!

How many such routes are there through a 20×20 grid?

"""
1 1 1
1 2 3
1 3 6

0 0 0
0 0 0
0 0 0

#I think this is pascals triangle variant iirc
1	1	1	1	1	1	
1	2	3	4	5	6
1	3	6	10	15	21
1	4	10	20	35	56
1	5	15	35	70	126
1	6	21	56	126 252

# construct an empty matrix of 20 x 20

# to arrive at the total for that cell


def build_grid(size_tuple):
	col = [0 for x in range(size_tuple[1])]
	rows = [col for x in range(size_tuple[0])]
	return rows

def fill_ones(grid):
	""" make the first row and the first column all ones """	
	grid[0] = [1 for x in grid[0]]
	return grid

def traverse_paths(grid):
	for i in range(1, len(grid)):
		for j in range(0, len(grid[0])):
			if j == 0:
				grid[i][j] = 1
			else:
				grid[i][j] = (grid[i-1][j]) + (grid[i][j-1])

	return grid


def grid_path_num(size_tuple):

	grid = build_grid(size_tuple)
	grid = fill_ones(grid)
	grid = traverse_paths(grid)

	return grid[(size_tuple[0]-1)][(size_tuple[1]-1)]


x = grid_path_num((21,21))
x

import numpy as np

grid = np.zeros((21,21))
grid[0,] = 1
grid[:,0] = 1
grid

grid.shape
for i in range(1,grid.shape[0]):
	for j in range(1,grid.shape[1]):
		grid[i,j] = (grid[i-1,j] + grid[i, j-1])

grid[20,20]

#137846528820