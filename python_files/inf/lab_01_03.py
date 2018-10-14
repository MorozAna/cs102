'''
 Форматированный ввод/вывод данных
'''
m = 10
pi = 3.1415927
print("m =", m)
print("m = %d" % m)
print("%7d" % m)
print("pi = ", pi)
print("%.3f" % pi)
print("%10.4f\n" % pi)
print("m = {}, pi = {}".format(m,pi))
ch = 'A'
print("ch = %c" % ch)
s = "Hello"
print("s = %s" % s)
print("\n\n")
code = input("Enter your position number in group: ")
n1, n2 = input("Enter two numbers splitted by space: ").split()
d, m, y = input("Enter three numbers splitted by\'.\': ").split('.')
print("{} + {} = {}".format(n1,n2,float(n1)+float(n2)))
print("Your birthday is %s.%s.%s and you are %d in the group list" % (d,m,y,int(code)) )

print("m = %4s; pi =й:

int([object], [основание системы счисления]) - преобразование к целому числу в десятичной системе счисления. По умолчанию система счисления дес %.3f" % (m, pi))

print("m = {}; pi = {}".format(m, pi))

year = input("Enter your course number: ")
print("Your course number is {}".format(year))

r1, m1, p1 = input("Enter your scores in Russian, Math and English splitted by \',\': ").split(',')
print("r1 = {}; m1 = {}; p1 = {}".format(r1, m1, p1))

bday = int(input("Enter your birthday: "))
bday = int(bday/8+2)
num = input("Enter a 20-bit number in %d numeral system: " % bday)
print ("Your number in 10 numeral system is", int(num, bday))

numb = int(input("Enter an integer number: "))
print("Your number * 2 = {}\nYour number / 2 = {} ".format(numb<<1, numb>>1))