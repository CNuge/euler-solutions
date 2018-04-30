
"""
A common security method used for online banking is to ask the user for three random characters from a passcode. 
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; 
the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, 
analyse the file so as to determine the shortest possible secret passcode of unknown length.

https://projecteuler.net/problem=79

curl https://projecteuler.net/project/resources/p079_keylog.txt > p079_keylog.txt

"""

# I could eyeball this one... but I'll code a solution regardless
# count befores and afters for all pairs of markers... 


def add_to_list(list_of_lists, new_list):
	for x in list_of_lists:
		if x[-1] == new_list[0]:
			x.extend(new_list[1:])
	
	list_of_lists.append(new_list)
	return list_of_lists

		

if __name__ == '__main__':

	list_of_paths = []
	seen = set()

	with open('p079_keylog.txt') as file:
		for line in file:
			data = [int(x) for x in list(line.rstrip())]
			add_to_list(list_of_paths, data)
			seen = set(list(seen) + data)

	list_of_paths

	for x in list_of_paths:
		for y in list_of_paths:
			if x[-1] == y[1]:
				x.append(y[2])

	for x in list_of_paths:
		if len(x) == len(seen):
			print(x)
