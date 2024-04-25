k=[4,5,6,'ravi','sonu','kumar',66,77,88,'vipin']
j=1
p=[]
p1=[]
x=0
y=0
for i in k:
    if type(j)==type(i):
        x+=1
        p.append(i)
    else:
        y+=1
        p1.append(i)
print('Number of integer value ',x)
print('Number of string value ',y)
print(p)
print(p1)


#---------------------------------------------------------------------------------#


k2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime=[]
not_prime=[]
for i in k2:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        prime.append(i)
    else:
        not_prime.append(i)
print('prime: ',prime)
print('not prime: ',not_prime)



#-----------------------------------------------------------------------#

k3=[4,5,6,[6,7,8],55,66,77,['ravi','sonu'],88,99]
b=[]
c=0
for ele in k3:
    if (type(ele)==list):
        c+=1
        for j in ele:
            b.append(j)
    else:
        b.append(ele)

if type(k3)==list:
    c+=1
print("number of list in k3: ",c)
print(b)




#--------------------------------------------------------#

k=[22,55,66,77]
print(k)
k[0],k2[0],k[1],k[3]=k[2],k[0],k[3],k[1]
print('after swapping',k)
#---------------------------------------------------------------#

string= input("Enter the sting value to check whether it is a palindrome or not")

rev = string[::-1]
if string==rev:
    print("plaindrome")
else:
    print('not palindrome')



#--------------------------------------------------------------------#



num = int(input("Enter the number for check palindrome"))
num1=str(num)
if num1==num1[::-1]:
    print('palindrome')
else:
    print('not palindrome')


#--------------------------------------------------------------------#