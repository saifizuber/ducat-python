# constructor is a special method of your class
# constructor always same name  as class name
# constructor denoted by '__init__()'
# constructor are useful to allocate dynamic memory of your class
# constructor are useful to allocate dynamic memory of your class instance variable
# constructor cannot overload in python programming
# All variable and are declared in constructor are always global


# Two types method of constructor are
# 1. implicity constructor method
# 2. explicity constructor method


class Emp:
    def __init__(self,x,y,z,a): #parameterized constructor
        self.name = x
        self.lastname = y
        self.salary = z
        self.age = a

    def show(self):
        print('Emp name is ',self.name)
        print('Emp lastname is ',self.lastname)
        print('Emp salary is ',self.salary)
        print('Emp age is ', self.age)

name = input('Enter the name of Emp ')
lastname = input('Enter the lastname of Emp ')
salary = int(input("Enter the salary of Emp "))
age = int(input('Enter the age of Emp '))



k=Emp(name,lastname,salary,age)
k.show()
