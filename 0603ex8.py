a1 = 2
r = 2
an = a1
n = 1

while True:
    if an > 10000:
        break
    an = a1 * (r ** n)
    n += 1

print(f"{an} at position {n}")
