number = int(input("Enter a number: "))

if number % 5 == 0 or number % 7 == 0:
    if number % 8 == 0:
        print("You are a super winner")
    else:
        print("You are a winner")