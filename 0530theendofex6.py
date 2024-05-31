#Use the while loop to find the smallest number that is divisible by all integers from 1 to 9

number = 9

while True:
    div = True
    for divisor in range(1, 10):
        if number % divisor != 0:
            div = False
            break

    if div:
        print(number)
        break

    number += 9
