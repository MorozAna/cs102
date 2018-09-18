number = 23
running = True

while running:
	guess = int(input('Insert a number: '))

	if guess == number:
		print('Congratulations! You won!')
		running = False
	elif guess < number:
		print('No, it is greater.')
	else:
		print('No, too much.')
else:
	print("We're done with it")

print('Shutting down...')	