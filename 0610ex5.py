class Student:
    def __init__(self, name, dob, id, major, gpa=0):
        self.name = name
        self.dob = dob
        self.id = id
        self.major = major

student1 = Student('John', '1/1/2000', 'AU123', 'compact')
print (student1.name, student1.dob)



class Automobile:
    def __init__(self, tires, headlights, windshield):
        self.tires = tires
        self.headlights = headlights
        self.windshield = windshield

car = Automobile(tires=4, headlights=2, windshield=True)

print(f"Tires: {car.tires}")
print(f"Headlights: {car.headlights}")
print(f"Windshield: {car.windshield}")
