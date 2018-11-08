"""
The 5-digit number, 16807=75, is also a fifth power. 
Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

https://projecteuler.net/problem=63
"""

len_pow = 0

for i in range(1,1000):
	for j in range(1,100):
		n = i**j
		if len(str(n)) == j :
			len_pow +=1
			print(f'{i}**{j}:\t{len_pow}')

