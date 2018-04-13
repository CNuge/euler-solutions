"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


https://projecteuler.net/problem=14
"""



def collatz_len(integer):
	len_of_seq = 0

	while integer != 1:
		len_of_seq += 1

		if integer % 2 == 0:
			integer = integer/2
		else:
			integer = (3*integer)+1
	#when the loop condition not met, add one for the final 1 in the seq
	else:
		len_of_seq +=1

	return len_of_seq


def longest_collatz_seq(max_val):
	top_collatz = (1,1)
	for i in range(1,max_val):
		seq_len = collatz_len(i)
		if seq_len > top_collatz[1]:
			top_collatz = (i, seq_len)
	return top_collatz

longest_collatz_seq(1000000)

