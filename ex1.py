num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 > num2:
    if num1 > num3:
        print(num1, 'num1 is the greater number')
    else:
        print(num3, 'num3 is the greater number')
else:
    if num2 > num3:
        print(num2, 'num2 is the greater number')
    else:
        print(num3, 'num3 is the greater number')