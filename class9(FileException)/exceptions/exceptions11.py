print("First")
a = 5
b = 2
d = []
try:
    c = a/b
    e = d[5]
except ZeroDivisionError:
    print("Handel ZeroDivisionError")
except:
    print("Handle Error")
else:
    print(c)

print("last")

