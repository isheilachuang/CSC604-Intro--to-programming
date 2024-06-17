import myimportmodule

var1 = 2
var2 = 5
var3 = 34

sum = myimportmodule.sum_of_num(var1, var2, var3)
print(sum)

sum1 = myimportmodule.cube(var2)
print(sum1)

name = "ting"
print(myimportmodule.greet(name))

student1 = myimportmodule.Student("John", "Doe", "Computer Science")
print(student1.get_fname())