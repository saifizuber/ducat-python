#encapsulation = conbine all row data in single unit is known as encapsulation.
#                gave security to the code
#                no one access the code fo

class employee:
    salary = 8000
    def show(self):
        print(self.salary)


k=employee()
k.salary=3000
k.show()

#by defalut all memeber are public


#to make private member USE double underscore

class employee:
    __salary = 8000  #due to underscore '__' it is not change
    def show(self):
        print(self.__salary)


k=employee()
k.salary=3000
k.show()




#encapsulation using property method
#getter and setter are used for implement the property method
#this method is used for gave access to the admin

class emp:
    __sal = 7000
    def getter(self):
        return self.__sal
    def setter(self,x):
        self.__sal=x

k1=emp()
k1.setter(600)
print(k1.getter())

