from skimage import novice
from skimage import data
import numpy as np
from skimage.novice import Picture
from skimage import filters,io

img = novice.open('imgvin.jpg')

width = img.width
heigth = img.height


imageFinal =  Picture.from_size((heigth,width), color=(255, 255, 255))

def calcLine(value):
    return value*2+1

pixelsR = []
pixelsG = []
pixelsB = []

pad = 1
line = calcLine(pad)

for i in range(width):
    for j in range(heigth):
        for x in range(line):
            Xpos = i + (x - pad)
            for y in range(line):
                Ypos =  y + (j - pad)
                if(Xpos >= 0 and Xpos < width  and Ypos >=0 and Ypos < heigth):

                        pixelsR.append(int(img[Xpos,Ypos].red))
                        pixelsG.append(int(img[Xpos,Ypos].green))
                        pixelsB.append(int(img[Xpos,Ypos].blue))

        pixelsR = sorted(pixelsR)
        pixelsG = sorted(pixelsG)
        pixelsB = sorted(pixelsB)
        median = int((len(pixelsR)/2))
        imageFinal[i,j] = (pixelsB[median],pixelsG[median],pixelsR[median])


imageFinal.show()
