'''
1. instance variable
2. non instance variable(static variable)
3. static method(static method and call by class name), use for share , denoted by static decorator
4. instance method(dynamic method)
5. class method
'''


class Emp:

    company = 'NIIT'   #static variable(non instance variable), values are shareable of these variable

    def __init__(self,x,y,z,a): #parameterized constructor

        self.name = x #instance variable
        self.lastname = y
        self.salary = z
        self.age = a

    def show(self):  #instance method
        print('Emp name is ',self.name)
        print('Emp lastname is ',self.lastname)
        print('Emp salary is ',self.salary)
        print('Emp age is ', self.age)
        print('Emp company name is ',Emp.company)

    @staticmethod
    def ChangeAge(a):
        if(a<18):
            print('he is not employee')

        else:
            print('HE is a employee')

    @classmethod
    def ChangeCompany(cls):
        cls.company='Hcl'


n = input('Enter the name of Emp ')
l = input('Enter the lastname of Emp ')
s = int(input("Enter the salary of Emp "))
a = int(input('Enter the age of Emp '))



k=Emp(n,l,s,a)
Emp.ChangeAge(k.age) # static method calling with class name)
Emp.ChangeCompany()
k.show()


'''
static method
static method logic cannot change
denoted by static decorator

'''


'''
class method are useful to change the static variable value
class method will be call by class name'''