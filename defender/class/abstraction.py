# Abstraction => Abstraction show the external property and hide the internal property

# abstraction implement by abstract class

# abstraction already in the python

# abstraction class is not a pure incomplete class

# abstract class incomplete method implement in derived class(child class) and access by derived class object

# we can not create object of abstract class

# abstract class incomplete method denoted by '@' decorator

import random

from abc import abstractmethod
class emp:
    @abstractmethod
    def Daysalary(self,h,r):
        pass
    @abstractmethod
    def Monthsalary(self):
        pass
    @abstractmethod
    def ITR(self,y):
        pass
    @abstractmethod
    def Absent(self,a):
        pass
    @abstractmethod
    def Totalsal(self):
        pass

class Engineer(emp):
    def Daysalary(self,h,r):
        global d
        d=h*r
        print(d)
    def Monthsalary(self):
        global m
        m=d*30
        print(m)
    def ITR(self,y):
        global I
        I=m*y/100
        print(I)
    def Absent(self,a):
        global ab
        ab= d*a
        print(ab)
    def Totalsal(self):
        total = m-ab-I
        print(total)

n=Engineer()
n.Daysalary(5,1000)
n.Monthsalary()
n.ITR(5)
n.Absent(5)
n.Totalsal()


'''
create account 
pin code
withdraw amount 
deposit amount 
check balance
exit 
'''








class ATM:
    @abstractmethod
    def CreateAccount(self,name, accountNo, AadharNo, Branch):
        pass
    @abstractmethod
    def DepositAmount(self,bal):
        pass
    @abstractmethod
    def WithdrawAmount(self,amount):
        pass
    @abstractmethod
    def CheckBal(self):
        pass
    @abstractmethod
    def Exit(self):
        pass


class Bank(ATM):
    Balance = 0
    def __int__(self,x,z,a):
        self.name = x
        self.accountNo = random.randint(10000000,12341234342)
        self.AadharNo = z
        self.Brach = a

    def CreateAccount(self):
        print('Emp name is ',self.name)
        print('Emp accountNo. is ',self.accountNo)
        print('Emp AadharNo is ', self.AadharNo)
        print('Emp branch is ',self.Brach)
