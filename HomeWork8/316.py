a = "1467"
b = "5"
c = "11"
d = "12"

a2 = a[-1] + a[1:-1] + a[0]
b2 = b[-1] + b[1:-1] + b[0]
c2 = c[-1] + c[1:-1] + c[0]
d2 = d[-1] + d[1:-1] + d[0]

if len(a) == len(a2):
    print(a2)
else:
    print(a2[0])

if len(b) == len(b2):
    print(b2)
else:
    print(b2[0])

if len(c) == len(c2):
    print(c2)
else:
    print(c2[0])

if len(d) == len(d2):
    print(d2)
else:
    print(d2[0])