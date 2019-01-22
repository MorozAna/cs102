# Практическая работа

#### Задание 1: Скачайте файл с данными о погибших на титанике
import requests
import os

def to_str(lines: list) -> str:
    # Функция возвращает список преобразованных строк,
    # а принимает список байтовых строк
    
    # Отдельно взятую строку байт можно преобразовать в строку
    # символов следующим образом: str(line, 'utf-8')+'\n'
    # Символ перехода на новую строку добавляется, чтобы при
    # записи в файл каждая запись начиналась с новой строки
    
    # Удалите pass и представьте ваше решение
    string = ''
    for line in lines:
    	string += str(line, 'utf-8') + '\n'
    return string


def download_file(url: str) -> str:
    # Делаем GET-запрос по указанному адресу
    response = requests.get(url)
    # Получаем итератор строк
    text = response.iter_lines()
    # Каждую строку конвертируем из массива байт в массив символов
    text = to_str(text)

    # Если файла не существует, то создаем его и записываем данные
    if not os.path.isfile("titanic.csv"):
        with open("titanic.csv", "w") as f:
            f.writelines(text)
    return text

#data = download_file("https://raw.githubusercontent.com/haven-jeon/introduction_to_most_usable_pkgs_in_project/master/bicdata/data/titanic.csv")

# Если вы успешно выполнили первое задание, то файл можно не скачивать
# каждый раз, а вместо этого данные читать из файла. Расскомментируйте
# следующую строку и закомментируйте предыдущую
data = open('titanic.csv')

#### Задание 2: Получаем список словарей
# Модуль для работы с файлами в формате CSV
import csv

reader = csv.DictReader(data)
reader.fieldnames[0] = 'lineno'
titanic_data = list(reader)

# Модуль для красивого вывода на экран
from pprint import pprint as pp
pp(titanic_data[:2])
pp(titanic_data[-2:])


#### Задание 3: Узнать количество выживших и погибших на Титанике

def survived(tit_data: list) -> tuple:
    # Функция возвращает кортеж из двух элементов: количество
    # выживших и число погибших
    '''
    >>> survived(titanic_data)
    (500, 809)
    '''
    a = 0
    b = 0
    for i in tit_data:
    	if i['survived'] == "1":
    		a += 1
    	else:
    		b += 1
    return (a, b)

pp(survived(titanic_data)) # (500, 809)


#### Задание 4: Узнать количество выживших и погибших на Титанике
#### по отдельности для мужчин и женщин
from operator import itemgetter
from itertools import groupby
def survived_by_sex(tit_data: str) -> list:
    # Функция возвращает список кортежей из двух элементов вида:
    # (пол, (количество выживших, число погибших))

    # Подумайте над использованием функции survived()

    '''
    >>> survived_by_sex(titanic_data)
    [('male', (161, 682)), ('female', (339, 127))]
    '''
    m = []
    f = []
    for i in tit_data:
    	if i['sex'] == "male":
    		m.append(i)
    	else:
    		f.append(i)
    ms = survived(m)
    fs = survived(f)
    return [('male', ms), ('female', fs)]

pp(survived_by_sex(titanic_data)) # [('female', (339, 127)), ('male', (161, 682))]


#### Задание 5: Узнать средний возраст пассажиров
def average_age(tit_data: str) -> str:
    # Функция возвращает средний возраст пассажиров
    '''
    >>> average_age(titanic_data)
    '29.88'
    '''
    a = 0
    count = 0
    for i in tit_data:
    	if i['age'] != 'NA':
    	    a += float(i['age'])
    	    count += 1
    b = a / count
    return "%.2f" % b 

pp(average_age(titanic_data)) # 29.88


#### Задание 6: Узнать средний возраст мужчин и женщин по отдельности
def average_age_by_sex(tit_data: str) -> list:
    # Функция возвращает список кортежей из двух элементов вида:
    # (пол, средний возраст)

    # Подумайте над использованием функции average_age()
    '''
    >>> average_age_by_sex(titanic_data)
    [('male', '30.59'), ('female', '28.69')]
    '''
    m = []
    f = []
    for i in tit_data:
    	if i['sex'] == "male":
    		m.append(i)
    	else:
    		f.append(i)
    ma = average_age(m)
    fa = average_age(f)
    return [('male', ma), ('female', fa)]

pp(average_age_by_sex(titanic_data)) # [('female', 28.69), ('male', 30.59)]


#### Задание 7: Сколько детей и взрослых было на борту:
#### Получить группы в следующих диапазонах возрастов:
#### [0-14), [14-18), [18-inf]
def count_ages(tit_data: str) -> str:

	'''
	>>> count_ages(titanic_data)
	'Small chidren: 99, Teens: 55, Adults: 892'
	'''

	small = 0
	middle = 0
	big = 0
	for i in tit_data:
		if i['age'] != 'NA':
			if float(i['age']) < 14:
				small += 1
			elif float(i['age']) < 18:
				middle += 1
			else:
				big += 1
	return ('Small chidren: {}, Teens: {}, Adults: {}'.format(small, middle, big))

pp(count_ages(titanic_data))

#### Задание 8: Сколько в каждой группе выживших
def count_surs_by_age(tit_data: str) -> str:

	'''
	>>> count_surs_by_age(titanic_data)
	'Small chidren: (57, 42), Teens: (24, 31), Adults: (346, 546)'
	'''

	small = []
	middle = []
	big = []
	for i in tit_data:
		if i['age'] != 'NA':
			if float(i['age']) < 14:
				small.append(i)
			elif float(i['age']) < 18:
				middle.append(i)
			else:
				big.append(i)
	small_s = survived(small)
	middle_s = survived(middle)
	big_s = survived(big)
	return ('Small chidren: {}, Teens: {}, Adults: {}'.format(small_s, middle_s, big_s))

pp(count_surs_by_age(titanic_data))

#### Задание 9: Сколько в каждой группе выживших по отдельности для
#### мужчин и женщин

def final(tit_data: str) -> str:

	'''
	>>> final(titanic_data)
	'Small chidren: male (28, 25) female (29, 17); Teens: male (3, 26) female (21, 5); Adults: male (104, 472) female (242, 74)'
	'''

	small = []
	middle = []
	big = []
	small_m = []
	middle_m = []
	big_m = []
	small_f = []
	middle_f = []
	big_f = []
	for i in tit_data:
		if i['age'] != 'NA':
			if float(i['age']) < 14:
				small.append(i)
			elif float(i['age']) < 18:
				middle.append(i)
			else:
				big.append(i)
	for i in small:
		if i['sex'] == 'male':
			small_m.append(i)
		else:
			small_f.append(i)
	for i in middle:
		if i['sex'] == 'male':
			middle_m.append(i)
		else:
			middle_f.append(i)
	for i in big:
		if i['sex'] == 'male':
			big_m.append(i)
		else:
			big_f.append(i)
	small_fs = survived(small_f)
	small_ms = survived(small_m)
	middle_fs = survived(middle_f)
	middle_ms = survived(middle_m)
	big_fs = survived(big_f)
	big_ms = survived(big_m)
	return "Small chidren: male {} female {}; Teens: male {} female {}; Adults: male {} female {}".format(small_ms,small_fs,middle_ms,middle_fs,big_ms,big_fs)

pp(final(titanic_data))
