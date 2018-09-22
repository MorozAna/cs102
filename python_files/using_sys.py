import sys

print('Command arguments: ')
for i in sys.argv:
	print(i)

print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')