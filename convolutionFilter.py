from skimage import novice
from skimage import data
import numpy as np
from skimage.novice import Picture

img = novice.open('flower.jpg')


#print(img)

width = img.width
heigth = img.height

#print(width)
#print(heigth)


matrizWeigths = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]

widthWeigths = len(matrizWeigths)
heigthWeights = len(matrizWeigths[1])


newImage = np.zeros(shape=(width,heigth,3),dtype=np.uint8)

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

somaR = 0
somaG = 0
somaB = 0

weigthMatriz = getSomaPesos(matrizWeigths)
print(weigthMatriz)

'''for i in range(width):
    for j in range(heigth):
        r = int(0.21*img[i][j][2])
        g = int(0.72*img[i][j][1])
        b = int(0.07*img [i][j][0])

        aux = b+g+r

        img[i][j] = [aux,aux,aux]
'''

weigthMatriz = 1 if weigthMatriz == 0 else weigthMatriz


for i in range((width - widthWeigths)):
    for j in range((heigth - heigthWeights)):

        somaR = 0
        somaG = 0
        somaB = 0

        for x in range(widthWeigths):
            for y in range(heigthWeights):
                r = int(img[i+x,y+j].red)
                g = int(img[i+x,y+j].green)
                b = int(img[i+x,y+j].blue)

                somaR += r * matrizWeigths[x][y]

                somaG += g * matrizWeigths[x][y]
                somaB += b * matrizWeigths[x][y]


        somaR = int(somaR/weigthMatriz)
        somaG = int(somaG / weigthMatriz)
        somaB = int(somaB / weigthMatriz)

        somaR = 0 if somaR  < 0 else somaR
        somaR = 255 if somaR > 255 else somaR

        somaB = 0 if somaB < 0 else somaB
        somaB = 255 if somaB > 255 else somaB

        somaB = 0 if somaB < 0 else somaB
        somaB = 255 if somaB > 255 else somaB

        #print(somaR)
        newImage[i,j] = (somaR,somaR,somaR)





print(img)
imagenResult = Picture(array=newImage)
imagenResult.show()
