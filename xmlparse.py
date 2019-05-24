import xml.dom.minidom as xm
doc=xm.parse("full.xml")
contents=doc.getElementsByTagName("Contents")
f = open("keylist.txt", 'w')

for content in contents:
    key=content.getElementsByTagName("Key")[0]
    f.write(key.firstChild.data + '\n')

f.close()
