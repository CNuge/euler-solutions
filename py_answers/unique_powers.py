
#quick in py to double check

pow_list = []

for i in range(2, 101):
	for j in range(2,101):
		pow_list.append(i**j)

len(set(pow_list))