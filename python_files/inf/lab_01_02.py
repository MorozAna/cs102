'''
 Логические операции
'''
f = True
g = False
print("f: ", f)
print("not f: ", not f)
print("f and g: ", f and g)
print("f or g: ", f or g)
print("f == g: ", f == g)
print("f != g: ", f != g)
print("\n")
h = 3
i = 5
print("h = ", h)
print("i = ", i)
print("h > i: ", h > i)
print("h < i: ", h < i)
print("h >= i: ", h >= i)
print("0 < h <= i: ", 0 < h <= i)
print("\n\n")
'''
 Побитовые операции
'''
j = 7
k = 20
print("j = %d; j in binary format: %s" % (j, bin(j)))
print("k = %d; k in binary format: %s" % (k, bin(k)))
print("j & k: %d; binary: %s" % (j & k, bin(j & k)))
# побитовое AND
print("j | k: %d; binary: %s" % (j | k, bin(j | k)))
# побитовое OR
print("j ^ k: %d; binary: %s" % (j ^ k, bin(j ^ k)))
# побитовое XOR
print("~k: %d; binary: %s" % (~k, bin(~k))) 
#инверсия двоичного числа
print("k>>1: %d; binary: %s" % (k>>1, bin(k>>1))) 
#сдвиг на один бит вправо
print("k<<1: %d; binary: %s" % (k<<1, bin(k<<1))) 
#сдвиг на один бит влево
print("\n\n")

A = 5
B = 2
C = True
D = False

print("not (C and D) =", not (C and D))
print("C and D or not(C and D) =", C and D or not(C and D))
print("not C or D =", not C or D)

print("A <= B =", A <= B)
print("A > B and A == B =", A > B and A == B)
print("not (A < B) =", not (A < B))

s = 154
p = 6
print("s = %d; s in binary format: %s" % (s, bin(s)))
print("p = %d; p in binary format: %s" % (p, bin(p)))
print("s | p: %d; binary: %s" % (s | p, bin(s | p)))

s = s>>2
p = p>>2
print("s = %d; s in binary format: %s" % (s, bin(s)))
print("p = %d; p in binary format: %s" % (p, bin(p)))