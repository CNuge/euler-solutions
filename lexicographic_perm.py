"""

A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 

0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


https://projecteuler.net/problem=24

"""

from itertools import permutations

digits = ['0','1','2','3','4','5','6','7','8','9',]

all_perms = [''.join(x) for x in permutations(digits)]

len(all_perms)

sorted_perms = sorted(all_perms)

sorted_perms[999999]
