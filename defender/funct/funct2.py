# import funtion

# print(funtion.cub(5))

def dele(x,y):  #parameterized funtion
    s=x[y:]
    print(s)

k=[1,2,3,4,5,65,7,7,8,8,9,0]

dele(k,4)


def add():       #non parameterized funtion
    x=17860
    y=2345
    print(x+y)

add()


def show(id,name,lastname,age=20): #default function
    print('Emp id is ',id)
    print('Emp name is ', name)
    print('Emp lastname is ', lastname)
    print('Emp age is ', age)

show(333,'Mohd','Zuber')


def show(id, name, lastname, age):  # position argument function
    print('Emp id is ', id)
    print('Emp name is ', name)
    print('Emp lastname is ', lastname)
    print('Emp age is ', age)


show(name='ravi',id=555,age=20,lastname='kumar')   #we don't have to write function arguments in serial format just write the var name of funtion that argument you want to pass.



p=lambda x,y:x+y   #anonymous function or inline function
print(p(5,4)) #can't apply loop and conditional statement


#syntax of lambda

# lambda var_name: logic or condition, iteration,list which is used in logic


#find the 18% of salary
k=[40000,50000,60000,70000,80000,90000,100000,110000,120000]

t=list(map(lambda x:x*18/100,k))  #map take 2 argument and we have to use the map with list for getting output other wise it shows the error
print(t)



k=[40000,50000,60000,70000,80000,90000,100000,110000,120000]
n=[2,5,3,2,4,7,8,3]  #this is percentage list 'n' for every element of list 'k'
t=list(map(lambda x,y:x*y/100,k,n))    #k value goes to var x and n value goes to y
print(t)



k=[40000,50000,60000,70000,80000,90000,100000,110000,120000]

li=list(map(lambda x:x>40000 and x<70000,k)) # map print boolean value when give this type of logic
p=list(filter(lambda x:x>40000 and x<70000,k)) #filter is used of print actual value becoz map print the boolean value


print(li)
print(p)



#reduce funtion usend of merging

import functools

k=[3,4,5,6,7,8,9,1,8]
h=functools.reduce(lambda x,y:x+y,k)
print(h)
print(sum(k)) #this sum doing the same things


hi='hello ducat india this is python programming'

t=hi.split() #convert the string 'hi' into list

t.sort()  # sort the list data 't'
print(t)


hi=functools.reduce(lambda x,y:x+' '+y,t) #after sorting merge the list and make a string value

print(hi)
