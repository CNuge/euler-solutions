"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 

56623104 (384^3) and 66430125 (405^3). 

In fact, 41 063  is the smallest cube which has exactly three permutations of 
its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

https://projecteuler.net/problem=62

"""

from itertools import permutations

def cube_root(x):
	return int(round(x ** (1. / 3)))

def perfect_cube(x):
    return cube_root(abs(x)) ** 3 == x

def list_of_cubes(max):
	cube_list = []
	for x in range(0, max):
		val = x ** 3
		cube_list.append(val)
	return cube_list


def five_cube_perm(cube_list):

	for x in cube_list:
		print(x)
		str_x = str(x)
		count_perms = 0
		for i in permutations(str_x):
			number = int(''.join(i))			
			if perfect_cube(number): 
				count_perms += 1
		if count_perms == 5:
			return x


def split_cube_list(cube_list):
	""" take the cube list and split it by length """
	l_of_l = []
	
	str_cube_list = [ str(x) for x in cube_list]
	for i in range(len(str_cube_list[-1])):
		l = [x for x in str_cube_list if len(x) == i]
		l_of_l.append([int(x) for x in l])

	return l_of_l


def search_cube_list(list_of_cubes):
	for x in list_of_cubes:
		print(x)
		str_x = str(x)
		count_perms = 0
		for i in permutations(str_x):
			number = int(''.join(i))
			if number in list_of_cubes:
				count_perms += 1
		if count_perms == 5:
			return x
	return False


if __name__ == '__main__':


perfect_cube(41063625)
cube_root(41063625)


cube_list = list_of_cubes(10000)

answer = five_cube_perm(cube_list)
print(answer)

l_of_cube_sizes = split_cube_list(cube_list)

for x in l_of_cube_sizes:
	ans = search_cube_list(x)
	if ans != False:
		print(ans)




