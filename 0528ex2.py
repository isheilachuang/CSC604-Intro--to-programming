matrix1 = [[2,4,16], [3,9,81], [4,16,64]]

sum = 0
for x in matrix1:
    for y in x:
        sum = sum + y
        print(sum)

print(matrix1[1][1])
matrix1[2][1] = 21
print(matrix1)