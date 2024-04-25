'''
file handling are useful to
1. manipulate the file
2. delete the file
3. calculate the file
4. import and export the file with programming

'''

#how to create the file in python

'''
f= open("d://LIC.txt",'w')

f.write('chacha vidhayak h')

f.close()
'''

#read file

# f=open("D:\zuber.csv",'r')
# s=f.read()
# print(s)
# f.close()


import os
#os.remove("D:\LIC.txt") #remove file or delete file

#os.rename("D:\zuber.csv","D:\shaad.csv") # rename the file


f = open(r'C:\Users\mohdz\OneDrive\Desktop\zuber.txt', 'r')
# s=f.read()
# print(s)
# print(len(s))

s=f.readlines() #readlines in file
'''Print number of line in file'''
c=0
for i in s:
    c=c+1
print(c)
'''print number of word in the txt file'''
v=0
for i in s:
    t=i.split()
    p=len(t)
    v=v+p

print(v)

