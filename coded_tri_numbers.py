"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position 
and adding these values we form a word value. For example, 
the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing 
nearly two-thousand common English words, how many are triangle words?

curl https://projecteuler.net/project/resources/p042_words.txt > p042_words.txt

https://projecteuler.net/problem=42

"""

def letter_sum(word):
	letter_dict =  {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
    'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
    'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26
    }

	total = 0
	for x in word.lower():
		total += letter_dict[x]
	return total


def get_tri_list(top_tri):
	""" get a list of triangle numbers up to a maximal value"""
	tri_nums = [1]
	val = 1
	while tri_nums[-1] < top_tri:
		tri_val = int(.5*(val*(val+1)))
		tri_nums.append(tri_val)
		val += 1
	return tri_nums


def tri_number_count(list_of_words):
	""" take a list of words and determine the number of entries
		whose alphanumeric sums are triangle numbers """
	total = 0
	
	max_word_len = len(max(list_of_words, key=len))
	max_word_score = max_word_len * 26
	top_tri = int(.5*(max_word_score*(max_word_score+1)))
	
	tri_nums = get_tri_list(top_tri)

	for word in list_of_words:
		val = letter_sum(word)
		if val in tri_nums:
			total += 1

	return total


if __name__ == '__main__':

	file =  open('p042_words.txt', 'r')
	data = file.read()
	file.close()


	word_list = [x[1:-1] for x in data.split(',')]

	print(tri_number_count(word_list))
