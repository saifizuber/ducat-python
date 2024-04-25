# import pandas as pd
# a=int(input('Enter the number of key'))
# d={}

# for i in range(a):
#     p=[]
#     key=eval(input("Enter the key "))
#     n=int(input("enter the size of key "))
#     for j in range(n):
#         v=eval(input("enter the value "))
#         p.append(v)
#     d.setdefault(key,p)

# print(d)
# df=pd.DataFrame(d)
# df.to_csv("d://zuber.csv")



# d={i: i**2 for i in range(1,10)}
# print(d)

# t2={i:'even' if i%2==0 else 'odd' for i in range(1,10)}

# print(t2)

# t=['even' if i%2==0 else 'odd' for i in range (1,10)]
# print(t)

#assignment
# import pandas as pd
# dic_size = int(input("Enter the size of Table column wise: "))
# my_dict = {}

# for i in range(dic_size+1):
#     key = eval(input('Enter the key or heading of Stundent Table: '))
#     size_of_values = int(input('Enter the size of the key or heading of student table: '))
    
#     values = []
#     for j in range(size_of_values):
#         value = eval(input("Enter the value element: "))
#         values.append(value)
    
#     my_dict.setdefault(key, values)

# print(my_dict)
# df=pd.DataFrame(my_dict)
# print(df)


h='hello ducat india hello ducat my name gaurav'
h1=h.split()
print(h1)
b=[]
for i in h1:
    a=h1.count(i)
    b.append((i,a))
b1=list(set(b))
print(b)


dic = {'what is a java?':'highlevel','what is c?':'middle level','what is a python?':'dynamic'}

for i,j in dic.items():
    p=0
    print(i)
    x=input('enter the ans')
    while p<3:
        if (x==j):
            c+=1
            break
        else:
            print('try again')
            c-=1
        p+=1