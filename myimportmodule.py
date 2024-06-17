def sum_of_num(a, b, c):
    sum = a + b + c
    return(sum)


def cube(num):
    sum1 = num ** 3
    return(sum1)


def greet(name):
    return f"Hello {name}"


class Student:
    def __init__(self, fname, lname, major):
        self.fname = fname
        self.lname = lname
        self.major = major

    def get_fname(self):
        return(self.fname)


    def get_lname(self):
        return(self.lname)

    def get_major(self):
        return(self.major)

def sum_of_list(lst):
    return sum(lst)

