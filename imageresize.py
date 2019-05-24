import os
from os import walk
from PIL import Image
from resizeimage import resizeimage

def resize_file(in_path,out_path,size):
    with open(in_path,'r+b') as f:
        with Image.open(f) as image:
            cover=resizeimage.resize_thumbnail(image,size)
            cover.save(out_path,image.format)

# arr=os.listdir('.')
# print(arr)
# path="./"

arr=[]

for root, directories, filenames in os.walk('.'):
    for filename in filenames:
        arr.append(str(os.path.join(root,filename)))

arr.remove('.\\imageresize.py')
print(arr)

for i in arr:
    resize_file(i,i,[1920,1080])

# for i in arr:

# with Image.open('./grexter-images/buildings/7/1.jpg') as img:
#     width,height=img.size;
#     print(width,height)




# with open('./grexter-images/buildings/21/DSC_1845-compressor.jpg','r+b') as f:
#     with Image.open(f) as image:
#         cover=resizeimage.resize_contain(image,[1600,900])
#         cover.save('./grexter-images/buildings/21/DSC_1845-compressor1.jpg',image.format)