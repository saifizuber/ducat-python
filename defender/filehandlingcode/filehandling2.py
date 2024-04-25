import os

t=os.listdir('d://')  #listdir = list of directory

y=[]
s=[]
for i in t:
    if (i.endswith('.txt')):
        y.append(i)

    elif(i.endswith('.csv')):
        s.append(i)

print(len(y))  #count number txt file
print(len(s))  #count number csv file