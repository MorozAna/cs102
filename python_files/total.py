def total(*numbers, **keywords):
	count = 0
	for number in numbers:
		count += number
	for key in keywords:
		count += keywords[key]
	return count

print(total(10, 1, 2, 3, vegetables=50, fruit=100))