number = 23
guess = int(input('Insert a number: '))

if guess == number:
	print('Congrats, you guessed right')
	print("(didn't win anything tho!)")
elif guess > number:
	print('No, it is too much')
else:
	print('I need more!')

print("We're done here")