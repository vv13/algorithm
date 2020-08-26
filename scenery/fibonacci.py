a, b = (1, 1)
for i in range(int(input())):
    a, b = b, (a + b)
    print("index {0} is {1}".format((i + 3), b))
