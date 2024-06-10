def factorial(number):
    prod = 1
    if number %2 ==0:
        for x in range(1, number+1):
            prod = prod*x
    else:
        prod = number ** 4

    return(prod)

num = int(input("Enter the number for factorial here:"))
factorial_of_num = factorial(num)

print(f"The factorial of {num} is {factorial_of_num}.")