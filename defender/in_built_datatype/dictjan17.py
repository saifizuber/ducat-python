# x=int(input())
# d={}
# for i in range(x):
#     s=eval(input("Enter the key"))
#     v=eval(input("Enter the the values"))
#     d.setdefault(s,v)
# print(d)

import pandas as pd

di = {'id': [22, 33, 44], 'name': ['ravi', 'zuber', 'sonu'], 'age': [33, 22, 55]}
for i, j in di.items():
    print(i, "", j)

df = pd.DataFrame(di)
print(df)
df.to_csv("d://batch5pm.csv", index=False)
