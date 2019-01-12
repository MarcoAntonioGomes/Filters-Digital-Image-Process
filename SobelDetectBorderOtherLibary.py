from skimage import novice
from skimage import data
import numpy as np
import math
from skimage import data_dir
from skimage.novice import Picture
from skimage import filters,io
from skimage.io import imread


img = imread(data_dir + 'sobel.png', as_gray=True)

#print(img)

width = img.width
heigth = img.height

#print(width)
#print(heigth)

print(img)

KernelX = [[-1,0,1],[-2,0,2],[-1,0,1]]
print(KernelX)

KernelY = [[-1,-2,-1],[0,0,0],[1,2,1]]

print(KernelY)

widthWeigths = len(KernelX )
heigthWeights = len(KernelX )


matrizGx = Picture.from_size((heigth,width ), color=(255, 255, 255))
matrizGy =  Picture.from_size((heigth, width), color=(255, 255, 255))
imageFinal =  Picture.from_size((heigth,width), color=(255, 255, 255))

print(img[0,1])

def getElementCenter(matrizWeigths):
    x = len(matrizWeigths)
    y = len(matrizWeigths[0])
    return matrizWeigths[x-1][y-1]


def getSomaPesos(matrizWeigths):
    soma = 0
    for i in range(len(matrizWeigths)):
        for j in range(len(matrizWeigths[1])):
            soma += matrizWeigths[i][j]
    return soma;



weigthMatriz = getSomaPesos(KernelX)
print(weigthMatriz)

img.show()

'''for i in range(width):
    for j in range(heigth):
        r = int(0.21*img[i,j].red)
        g = int(0.72*img[i,j].green)
        b = int(0.07*img [i,j].blue)

        aux = b+g+r

        img[i,j] = (aux,aux,aux)

img.show()

'''

pad = (heigthWeights - 1)/2

for i in range((width - widthWeigths)):
    for j in range((heigth - heigthWeights)):

        somaRGx = 0
        somaGGx = 0
        somaBGx = 0
        divGx = 0

        somaRGy = 0
        somaGGy = 0
        somaBGy = 0
        divGy = 0

        for x in range(widthWeigths):
            for y in range(heigthWeights):

                Xpos = i + x - pad
                Ypos =  y + j - pad

                if(Xpos >= 0 and Xpos < width  and Ypos >=0 and Ypos < heigth):


                    r = int(img[i+x,y+j].red)
                    g = int(img[i+x,y+j].green)
                    b = int(img[i+x,y+j].blue)

                    somaRGx += r * KernelX[x][y]
                    somaGGx += g * KernelX[x][y]
                    somaBGx += b * KernelX[x][y]
                    divGx +=  KernelX[x][y]

                    somaRGy += r * KernelY[x][y]
                    somaGGy += g * KernelY[x][y]
                    somaBGy += b * KernelY[x][y]
                    divGy += KernelY[x][y]

        if(divGy == 0): divGy = 1
        if (divGx == 0): divGx = 1


        somaRGx = int(somaRGx/divGx)
        somaGGx = int(somaGGx / divGx)
        somaBGx = int(somaBGx /divGx)

        somaRGy = int(somaRGy / divGy)
        somaGGy = int(somaGGy / divGy)
        somaBGy = int(somaBGy / divGy)

        somaRGx = 0 if somaRGx < 0 else somaRGx
        somaRGy = 0 if  somaRGy < 0 else  somaRGy
        somaRGx = 255 if  somaRGx > 255 else somaRGx
        somaRGy = 255 if somaRGy > 255 else  somaRGy

        #print(somaR)
        matrizGx[i,j] = (somaRGx,somaRGx, somaRGx)
        matrizGy[i,j] = (somaRGy,somaRGy,somaRGy)




for i in range((width)):
    for j in range((heigth)):

        valueGX = matrizGx[i,j].red
        valueGY = matrizGy[i,j].red

        #valueGX = 255 if valueGX > 255 else valueGX
        #valueGY = 255 if valueGY > 255 else valueGY


        value = int(math.sqrt((valueGX**2)+(valueGY**2)))

        value = 255 if value > 255 else value
       # print(value)

        imageFinal[i,j] = (value,value,value)


#print(img)
imageFinal.show()
