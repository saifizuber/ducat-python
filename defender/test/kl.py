k2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
k=[4,5,6,66,77,88]
k1=k+k2
k1.sort()
s=0
print(k1)
for i in k1:
    s+=i
print(s)
res=s/len(k1)
print(res)