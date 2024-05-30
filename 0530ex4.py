sum2 = 0
i = 1

while i <= 100:
    for digit in str(i):
        sum2 += int(digit)
    i += 1

print(sum2)