
a1 = 2
r = 2

geometric_series = []

for n in range(1, 11):
    an = a1 * (r ** (n - 1))
    geometric_series.append(an)

print(geometric_series)
