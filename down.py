from urllib import request
keys=[]

file=open('keylist.txt','r')
for line in file:
    currentkey=line[:-1]
    keys.append(currentkey)

print(keys)
file.close()

for KEY in keys:
    f = open(KEY.replace("/",""), 'wb')
    try:
        f.write(request.urlopen("https://grexter-assets.s3-ap-southeast-1.amazonaws.com/"+KEY).read())
    except:
        pass
    f.close()