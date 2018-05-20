"""

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

https://projecteuler.net/problem=92
"""


def sum_dig_sq(number):
	total = 0

	for dig in str(number):
		total += int(dig) ** 2

	return total

def rep_add_sq(number):
	one_count, eighty_nine_count = -1, -1

	while one_count < 1 and eighty_nine_count < 1:
		number = sum_dig_sq(number)

		if number == 1:
			one_count += 1
		if number == 89:
			eighty_nine_count +=1			

	return one_count, eighty_nine_count



if __name__ == '__main__':
sum_dig_sq(44)

total_89_end = 0

for num in range(1,10000000):
	
	_ , eighty_nine_end = rep_add_sq(num)

	total_89_end += eighty_nine_end

print(total_89_end)
