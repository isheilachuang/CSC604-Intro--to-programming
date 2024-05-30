
n = int(input())

factorial = 1
num = 1

while num <= n:
    factorial *= num
    num += 1

print(f"The factorial of {n} is {factorial}")
