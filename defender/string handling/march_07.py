h='hello ducat india my name is gaurav'
#program for the sort the given string
'''t=h.split()

t.sort()

k=' '.join(t)

print(k)'''


print(h.startswith('hello'))  #output ture
print(h.endswith('gaurav'))   #input true




h='hello ducat 9810330542 india my name 913740312 is gaurav'
t=h.split()

k=[]
for i in t:
    if(i.isdigit()):
        k.append(i)
print(k)


h='hello ducat INDIA my name is ZUBER'
print(h.swapcase())




h='hello123'
print(h.isalnum())
print(h.istitle())
print(h.isnumeric())
print(h.isalpha())




H='#hello how are you#'

t=h.strip()
print(H)

'''
h.strip()  #remove space and charcter lke #@$ form both side(left and right)
h.lstrip() #remove left space and charcter like #$@
h.rstrip() #remove right space and charcter like #@$
'''


h='hello how are you this is ducat hello'

print(h.rfind('hello'))
print(h.find('hello'))
print(h[5:30])
print(h[5:30:2])



h='hello how@are you this@is ducat@hello'

print(h.rsplit('@',2))
print(h.split('@',2))