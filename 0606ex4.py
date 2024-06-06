def add_numbers(num1, num2, num3):
    print (num1, num2, num3)
    list1 = [num1, num2, num3]
    sqr = 0
    cub = 0
    total = 0
    for i in list1:
        if i%2==0:
            sqr = i**2
            total = total + sqr
        elif i%3 == 0:
            cub = i**3
            total = total + cub
        else:
            total = total+i

    return (total)

#main program
x = 10
y = 13
z = 21

sum = 0
sum = add_numbers(x, y, z) #calling the function
print (sum)

sum = add_numbers(2, 5, 3)
print (sum)