even_numbers = []
num = 0

while num < 101:
    if num % 2 == 0:
        even_numbers.append(num)
    num += 1

print(even_numbers)