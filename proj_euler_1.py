a = []

a.append(1)

a.pop()

for x in range(100000):
    if x % 2 == 0:
        a.append(x)
print(a)
