num = 9
numlist = []
while num < 9999999:
    if num%1 == 0 and num%2 == 0 and num%3 == 0 and num%4 == 0 and  num%5 == 0 and num%6 == 0 and num%7 == 0 and num%8 == 0 and num%9 == 0:
        numlist.append(num)
    num += 1
print(min(numlist))
