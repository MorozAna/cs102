# Это мой список покупок
shoplist = []

print('Что мне нужно купить?')
print('Введите покупки по одной, для продолжения похода в магазин введите "дальше" ')
while True:
	s = input()
	if s == 'дальше':
		break
	shoplist.append(s)

print('Я должен сделать ', len(shoplist), 'покупок.')

print('Покупки: ')
for item in shoplist:
	print(item, ' ')

print('Первое, что мне нужно купить, это', shoplist[0])
while len(shoplist) > 0:
	
	ans = 'no'
	while ans != 'да':
		print('Я купил ', shoplist[0], '?')
		ans = input()
		if ans == 'да':
			continue	

	print('Я купил', shoplist[0])
	olditem = shoplist[0]
	del shoplist[0]

	if len(shoplist) == 0:
		break
	
	print('Теперь мне нужно купить', shoplist[0])

print('Поход в магазин окончен. Хорошего дня!')	