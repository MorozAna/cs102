'''
 Форматированный ввод/вывод данных
'''
m = 10
pi = 3.1415927
print("m = ",m)
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
print("\n\n")

print("m = %4c" % m)
print("pi = %.3f" % pi)
print("m = {}, pi = {}".format(m,pi))
print("\n\n")

year = input("Enter your course: ")
print(f"You are on the {year} course.")
print("\n\n")

r1, m1, p1 = input("Enter your State Exam scores in Russian, Math and English splitted by\',\': ").split(',')
print(f"Your scores are: Russian {r1}, Math {m1}, English {p1}")
print("\n\n")

bday = int(input("Enter your birthday: "))
num = input("Enter a 12-bit number: ")
num = int(num, bday % 8 + 2)
print(num)
print("\n\n")

b = int(input("Enter a number: "))
print("b * 2 =", b<<1)
print("b / 2 =", b>>1)