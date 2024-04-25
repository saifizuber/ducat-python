import os


'''import time

t='d://batch4pm.txt'

ctim = os.path.getctime(t)
mtim = os.path.getmtime(t)

c_tim = time.ctime(ctim)
m_tim = time.ctime(mtim)

print(c_tim)
print(m_tim)

'''

f = open('d://batch4pm.txt','r')
s=f.readlines()

t=[]
for i in s:
    t.append(i)

t.pop(1)
h=' '.join(t)


f=open('d://batch4pm.txt','w')
f.write(h)


'''
find the word in which not having vowels from the file

 
k=['20,000$','4,000$','8,000$','5,000$']
find the sum of above list element

'''

h = 'my name is rythm i will try'

t=h.split()
k=['a','e','i','o','u','A','E','I','O','U']

u=[]
for i in t:
    for j in i:
        if(j in k):
            break
    else:
        u.append(i)
print(u)