# #we are taking two list of one for key element and another for one for value element
#
# k=['id','name','salary','age','contact'] #this is for key element
# k2=[222,'ravi',7000,20,800000] #this is for value element
# n=dict(zip(k,k2)) #method for conveting list to dict
# print(n)


#single list convert into dictionary

k=['ravi234','677sonu','vipin901','2anshul155']
p=[]
q=[]
for i in k:
    y=''
    s=''
    for j in i:
        if (j.isdigit()):
            y+=j
        else:
            s+=j
    p.append(y)
    q.append(s)
v=dict(zip(p,q))
