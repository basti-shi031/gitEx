import os,os.path
from PIL import Image,ImageOps

# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

def thumbnail(path):
    images = [x for x in os.listdir(path) if os.path.isfile(path+'/'+x) and (os.path.splitext(path+'/'+x)[1] == '.jpg' or os.path.splitext(path+'/'+x)[1] == '.png')]
    print(images)
    for imgName in images:
        img = Image.open(imgName)
        x,y = img.size
        sampleSizeX = 500
        sampleSizeY = y/x*500
        img = ImageOps.fit(img,(sampleSizeX,int(sampleSizeY)))
        img.save('result'+imgName)


path = '.'
thumbnail(path);