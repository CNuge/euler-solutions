
"""
For a number written in Roman numerals to be considered valid there are basic rules which 
must be followed. Even though the rules allow some numbers to be expressed in more than 
one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is 
considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one 
thousand numbers written in valid, but not necessarily minimal, Roman numerals; 
see About... Roman Numerals for the definitive rules for this problem.

#QUESTION:
Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than 
four consecutive identical units.


curl https://projecteuler.net/project/resources/p089_roman.txt > roman.txt

https://projecteuler.net/about=roman_numerals


https://projecteuler.net/problem=89

Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
I can only be placed before V and X.
X can only be placed before L and C.
C can only be placed before D and M.

#Examples:
MMMMDCLXXII
MMDCCCLXXXIII
MMMDLXVIIII
MMMMDXCV
DCCCLXXII
MMCCCVI
MMMCDLXXXVII
MMMMCCXXI
MMMCCXX
MMMMDCCCLXXIII
MMMCCXXXVII
MMCCCLXXXXIX
MDCCCXXIIII


# goal - find the number of characters saved by writing a number in its minimal form.
# need to calculate:
	#1. the number's value
	#2. the minimal form of that number
	#3. the character difference between the two (length of the strings)


Trick for parsing roman numerals:
- go right to left, this way we can keep track of the biggest numeral seen
then if a following value is smaller, we know to subtract it instead of adding it!

"""


def roman_to_numeric(numeral_string):
	""" take a valid roman numeral encoding and return its integer value """
	numeral_dict = dict(I = 1,
						V = 5,
						X = 10,
						L = 50,
						C = 100,
						D = 500,
						M = 1000)

	value = 0 #the total value of the numerals
	largest = 0 # to check if a numeral is lower than the highest seen value

	
	for char in numeral_string[::-1]:
		char_val = numeral_dict[char]
		if char_val < largest:
			value -= char_val
		else:
			largest = char_val
			value += char_val

	return value


def minimal_roman(integer):
	""" return a string that is the minimal representation of the number in
		roman numeral form """

	int_dict = {1 : 'I',
				5 : 'V',
				10 : 'X',
				50 : 'L',
				100 : 'C',
				500 : 'D',
				1000 : 'M'}

	num_count = {k : 0 for k in int_dict.keys() }

	for div in list(num_count.keys())[::-1]:
		if div <= integer:
			
			count = integer // div
			
			num_count[div] = count

			integer = integer % div

	num_string = ''

	for num, count in num_count.items():

		#should only see a 4 for base 10
		if count == 4 and num < 1000:
			
			if num_count[(num * 5)] == 1:
				addition = f'{int_dict[num]}{int_dict[(num * 10)]}'
				num_count[(num * 5)] = 0

			else:
				addition = f'{int_dict[num]}{int_dict[(num * 5)]}'

			num_string = addition + num_string

		else:
			addition = [int_dict[num] for n in range(0, count)]
			num_string =  ''.join(addition)  + num_string

	return num_string



if __name__ == '__main__':

	filename = 'roman.txt'

	char_saved = 0
	
	with open(filename) as file:
		for line in file:
			given_numeral = line.rstrip()

			value = roman_to_numeric(given_numeral)

			minimal_form = minimal_roman(value)

			size_dif = len(given_numeral) - len(minimal_form)

			char_saved += size_dif

	print(f'minimal encoding of the numbers would save: {char_saved} characters.\n')




"""
	fourty_four = 'XLIV'
	thirty_seven = 'XXXVII'
	nineteen = 'XIX'
	nineteen_b = 'XIIIIIIIII'
	nineteen_c = 'XVIIII'
	twenty_sixteen = 'MMXVI'
	nineteen_sixty_six = 'MCMLXVI'

	roman_to_numeric(fourty_four)
	roman_to_numeric(thirty_seven)
	roman_to_numeric(nineteen)
	roman_to_numeric(nineteen_b)
	roman_to_numeric(nineteen_c)
	roman_to_numeric(twenty_sixteen)
	roman_to_numeric(nineteen_sixty_six)


	#problem -  the current if clause correctly identifies the 'next up' reduction
	# need to identify the two up reductions as well. i.e. 9s
	minimal_roman(9)


	minimal_roman(1)
	minimal_roman(4)
	minimal_roman(19)
	minimal_roman(40)
	minimal_roman(41)
	minimal_roman(100)
	minimal_roman(1966)
	minimal_roman(2019)
	minimal_roman(1738)

"""




