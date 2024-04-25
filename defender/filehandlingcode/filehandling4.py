f=open('d://LIC.txt','r')

s=f.read()
x=input('enter the word you want search')

if (x in s):
    print('present')

else:
    print('not present')