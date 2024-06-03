a, b = 0, 1
fibonacci_series = []

for i in range(100):
    fibonacci_series.append(a)
    a, b = b, a + b

print(fibonacci_series)
