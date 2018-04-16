"""
If the numbers 1 to 5 are written out in words: 
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) 
inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 
342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
contains 20 letters. The use of "and" when writing out numbers is in compliance with 
British usage.

https://projecteuler.net/problem=17
"""

def increment_num_dict(number):
	number['ones'] += 1
	if number['ones'] == 10 :
		number['ones'] = 0
		number['tens'] += 1

	if number['tens'] == 10:
		number['tens'] = 0
		number['hund'] += 1

	if number['hund'] == 10:
		number['hund'] = 0
		number['thou'] += 1		

	return number
	

def num_string_build(number):
	ones_dict = { 0 : '',  
				1:  'one',
				2:  'two',
				3:  'three',
				4:  'four',
				5:  'five',
				6:  'six',
				7:  'seven',
				8:  'eight',
				9:  'nine',
				10: 'ten',
				11: 'eleven',
				12: 'twelve',
				13: 'thirteen',
				14: 'fourteen',
				15: 'fifteen',
				16: 'sixteen',
				17: 'seventeen',
				18: 'eighteen',
				19: 'nineteen',
				}

	tens_dict = { 
				0:'',
				2: 'twenty',
				3: 'thirty',
				4: 'forty',
				5: 'fifty',
				6: 'sixty',
				7: 'seventy',
				8: 'eighty',
				9: 'ninety',
				}

	outstring = ''

	if number['thou'] > 0:
		outstring += ones_dict[number['thou']]
		outstring += 'thousand'
		if number['hund'] != 0 or number['tens'] != 0 or number['ones'] != 0:
			outstring += 'and'

	if number['hund'] > 0 :
		outstring += ones_dict[number['hund']]
		outstring += 'hundred'
		if number['tens'] != 0 or number['ones'] != 0:
			outstring += 'and'

	if number['tens'] > 1:
		outstring += tens_dict[number['tens']]

	elif number['tens'] == 1:
		num = 10 +  number['ones']
		outstring += ones_dict[num]
	
	if number['ones'] != 0 and number['tens'] != 1:
		outstring += ones_dict[number['ones']]

	return outstring


def number_total_sub_1000(number_dict):

	total_char = 0
	while number_dict['thou'] < 1:

		number_dict = increment_num_dict(number_dict)

		numstring = num_string_build(number_dict)

		total_char += len(numstring)

	return total_char


if __name__ == '__main__':
	#thou,hund,ten,ones
	number_dict = {'thou':0,
					'hund': 0,
					'tens' :0,
					'ones': 0}

	print(number_total_sub_1000(number_dict))
