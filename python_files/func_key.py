def func(a, b = 5, c = 10):
	print("a equals", a, ", b equals", b, ", c equals", c)

func(3, 7)
func(25, c = 24)
func(c = 50, a = 100)