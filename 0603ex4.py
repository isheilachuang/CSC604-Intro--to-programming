a =1
b = 1
count = 3
fib = [a, b]
print('first term = ', a)
print('second term = ', b)

# sum = 0
# while count <= 100:
#     next_term = a+b
#     fib.append(next_term)
#     a=b
#     b = next_term
#     #  a,b = b, next_term
#     count += 1
# print(fib)

while True:
    next_term = a+b
    print(count, 'th term =', next_term)
    a,b = b, next_term  # this is the swap statement -> a=b + b = next_term
    count+= 1 # this is the same as count = count + 1
    fib.append(next_term)
    if(count == 10):
        break
print(fib)

# Exercise:
#  Find the sum of the first 100 terms of the Fibonacci series.
#  start with a = 1 and b = 1

a=1
b=1
count = 2
fib = [a,b]

sum1 = a+b

while count < 5:
    next_term = a+b
    fib.append(next_term)
    a,b = b, next_term
    count += 1
    sum1 = sum1 + next_term

print(fib)
print(sum1)
print(sum(fib))



# Exercise:
# need the first term and the difference to find all the other terms of the series
# First term a1 = 1
# Difference d = 3
# nth term a n = a1 + (n-1)*d
# (n is the term number)

# Use while loop to find first 10 terms
# [1, 4, 7, 10, 13, 16, 19, 22, 25]

# a1 = 1
# d = 3
# terms = []
# n = 1
#
# while n <= 9:
#     an = a1 + (n - 1) * d
#     terms.append(an)
#     n += 1
# print(terms)


# Now try with difference a1 and d values for example a1 =1 and d = 6
# [1, 7, 13, 19, 25, 31, 37]

a1 = 1
d = 6
terms = []
n = 1

while n <= 7:
    an = a1 + (n - 1) * d
    terms.append(an)
    n += 1
print(terms)




