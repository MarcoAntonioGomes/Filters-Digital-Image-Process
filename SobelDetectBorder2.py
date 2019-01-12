from skimage import novice
from skimage import data
import numpy as np
import math
from skimage.novice import Picture

img = novice.open('sobel.png')


#print(img)

width = img.width
heigth = img.height

for i in range(width):
    for j in range(heigth):
        r = int(0.21*img[i,j].red)
        g = int(0.72*img[i,j].green)
        b = int(0.07*img [i,j].blue)

        aux = b+g+r

        img[i,j] = (aux,aux,aux)

img.show()

width = img.width - 2
heigth = img.height - 2

stride = width
offset = stride + 1


