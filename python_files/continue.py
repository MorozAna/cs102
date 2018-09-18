while True:
	s = input("Insert smth: ")
	if s == "Quit":
		break
	if len(s) < 3:
		print('More')
		continue
	print("That's enough")