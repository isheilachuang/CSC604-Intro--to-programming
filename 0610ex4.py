class Student:
    name = ""
    dob = ""
    id = ""
    major = ""


#main program starts here

#create an instance of this Student class.
student1 = Student()

print (type(student1))

# #assign data/values to the class attribute

student1.name = "narendra"
student1.dob = "1/1/1990"
student1.id = "au125"
print (student1.name, student1.id, student1.dob)