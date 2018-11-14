def group(values, n):
	"""
	Сгруппировать значения values в список, состоящий из списков по n элементов

	>>> group([1,2,3,4], 2)
	[[1, 2], [3, 4]]
	>>> group([1,2,3,4,5,6,7,8,9], 3)
	[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	"""
	groups = []
	a = []
	count = len(values) // n
	i = 0
	for j in range(count):
		while len(a) < n:
			a.append(values[i])
			i += 1
		groups.append(a)
		a = []
	return groups

group([1,2,3,4,5,6,7,8], 3)