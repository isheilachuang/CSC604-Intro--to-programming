a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
c = float(input("Enter the third number (c): "))
d = float(input("Enter the fourth number (d): "))

if a >= b and a >= c and a >= d:
    print('a', a, 'is the greatest')
elif b >= a and b >= c and b >= d:
    print('b', b, 'is the greatest')
elif c >= a and c >= b and c >= d:
    print('c', c, 'is the greatest')
else:
    print('d', d, 'is the greatest')