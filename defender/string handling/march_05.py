'''

# string is a group of character
# string is in order format
# string is a static
# space is a character
# string is immutable

'''
h='hello ducat india'

print(h.upper()) #uppercase

print(h.lower()) #convert to lowercase

print(h.capitalize()) #convert first character to the capital

print(h.title()) #convert all word first letter capital

print(len(h)) #find the length of string





#program to count the total character without space
c=0
for i in h:
    if(i!=' '):
        c+=1
print(c)


#program for reversing the string
x=h[::-1]
print(x)