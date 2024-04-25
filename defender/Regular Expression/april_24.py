#REGULAR EXPRESSION

# it is pattern programming
# like mobile number:- mobile number of 10 digit
# gmail :- .com
# country code:-
# date format:- dd/mm/yyyy  31/12/
# THESE ALL PATTERN A MADE BY REGULAR EXPRESSION


import re    #re Reglar Expression

k='The rain in Spain'
x=re.search('^The.*Spain$',k)  # '.*' use for all in between

if(x):
    print('yes')
else:
    print('no match')

k='The Spain'
x=re.search('^The Spain$',k)

if(x):
    print('yes')
else:
    print('no match')


k='The rain in Spain'
x=re.search('^The Spain$',k)

if(x):
    print('yes')
else:
    print('no match')


#match particular expression like in 'ai' in string
k='The rain in Spain'
x=re.search('ai',k)

if(x):
    print('yes')
else:
    print('no match')




k='The@rain in@Spain@My name is@gaurav tomar'
x=re.split('@',k,2)
print(x)




k='The@rain in@Spain@My name is@gaurav tomar'
x=re.sub('@','88',k)
print(x)



k='The@rain in@Spain@My name is@gaurav tomar'
x=re.sub('@','88',k,2)
print(x)


t='^gau...s$'
test = 'gaukkks'
k=re.match(t,test)

if k:
    print('match')
else:
    print('no match')

#gmail format matching

line='mohdzuber0777@gmail.com'

email=re.findall()
if email:
    print('match')
else:
    print('no match')