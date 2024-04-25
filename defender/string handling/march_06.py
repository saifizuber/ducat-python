k='hello ducat india how are you hello how hello'

#count the frequency of every word
t=k.split()
y=[]
for i in t:
    if(i not in y):
        y.append(i)
        j=k.count(i)
        print(i,j)
print(y)






k='hello how are YOU MY name is ZUBER'

#separete the capital and non capital word from the given string
t=k.split()
k2=[]
k3=[]
for i in t:
    if(i.isupper()):
        k2.append(i)
    else:
        k3.append(i)

print(k2)
print(k3)




k='hello123 my name is zuber345saifi this is python986'
#separate the number and string from the given string

t=k.split()

h=[]
for i in t:
    p=''
    for j in i:
        if(j.isdigit()):
            p=p+j
    if(p!=''):
        h.append(p)
print(h)





k='hello my name is this is python this is gaurav this is java hi'
t=k.split()

t[4]='raman'

t[10]= 'noida'
p=' '.join(t)
print(p)



#print word that has length greater than 5
h=[]
for i in t:
    if(len(i)>5):

        h.append(i)
print('the word has length greater than 5')
print(h)