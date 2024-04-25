import csv

# f=open('d://pp.csv','w')
# s=csv.writer(f)
# s.writerow(['id','name','lastname','salary'])
# s.writerow([4334,'raju','kumar',50000])
# s.writerow([555,'mohd','zuber',70000])

# s=open('d://kundan.csv','w',newline='')  #newline used for give no gap between the two rows
# s=csv.writer(s)
# s.writerow(['id','name','lastname','salary'])
# s.writerow([4334,'raju','kumar',50000])
# s.writerow([555,'mohd','zuber',70000])


'''f=open('d://kundan.csv','r')
s=csv.reader(f)
for i in s:
    print(i)'''





'''    Read and Write Binary File     '''

'''k=[5,4,5,6,5,5,4,45,23,4,55,7,6,76,45,45,56,67,7,8,6]


g=open('d://binary.dat','wb')

g.write(bytes(k))'''   #write

j=open('d://binary.dat','rb')
f=list(j.read())  # read
print(f)



'''w+ = write and read
   r+ = read and write 
'''


#code for w+
'''f=open('d://rythm.txt','w+')
f.write('Hello i am Mohd Zuber')
f.seek(0)  #seek(0) is shift the pointer to zero position 
s=f.read()
print(s)
f.close()
'''

#code for r+

f=open('d://rythm.txt','r+')

s=f.read()
print(s)
f.seek(len(s)+1)
f.write('goods carrier train things')
