a = "Ada"
b = "Able was I ere I saw Elba"
c = "10501"
d = "Origin"

a2 = a.split(" ")
b2 = b.split(" ")
c2 = c.split(" ")
d2 = d.split(" ")

a3 = ""
b3 = ""
c3 = ""
d3 = ""

for i in a2:
    a3 += i
for i in b2:
    b3 += i
for i in c2:
    c3 += i
for i in d2:
    d3 += i

if a3.upper() == a3.upper()[::-1]:
    print("True")
else:
    print("False")

if b3.upper() == b3.upper()[::-1]:
    print("True")
else:
    print("False")

if c3.upper() == c3.upper()[::-1]:
    print("True")
else:
    print("False")

if d3.upper() == d3.upper()[::-1]:
    print("True")
else:
    print("False")