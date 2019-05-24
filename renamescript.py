import os
key="10 "
arr=os.listdir('.')
print(arr)

for i in arr:
    os.rename(i,i.replace(key,""))

print("Success")
