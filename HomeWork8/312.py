a = "euro"
b = "r"
c = a.split(b)
num = 0

if c[0] == a:
    num = -1
else:
    for i in range(len(c[0])):
        num += 1

print(num + 1)