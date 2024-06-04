# Exercise:
# tl = 1
# Nth triangular number Tn = (n *(n+1))/2
# Second triangular number T2 = 2 *(2+1)/2 = 2*3/2 = 3
# 3rd triangular number T3 = 3(3+1)/2 = 3*4/2 = 6
# Write a while loop to find the first 10 triangular numbers

tl = 1
N = tl + 1
n = 1
Tn =[]

while n <= 10:
    triangle_number = (N *(N+1))//2
    Tn.append(triangle_number)
    N += tl + 1
    n += 1
print(Tn)



# Exercise:
# Use the for loop to generate the first 100 Fibonacci series terms
a, b = 0, 1
fibonacci_series = []

for i in range(5):
    fibonacci_series.append(a)
    a, b = b, a + b

print(fibonacci_series)