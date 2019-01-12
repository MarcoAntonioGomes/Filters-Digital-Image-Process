import cv2
import numpy as np

img = cv2.imread('imgvin.jpg')



width = img.shape[0]
heigth = img.shape[1]


matrizWeigths = [[0,-1,0],[-1,5,-1],[0,-1,0]]

widthWeigths = len(matrizWeigths)
heigthWeights = len(matrizWeigths[1])






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

newImage = np.ndarray(img.shape, dtype=np.float)
print(newImage)

for i in range(width):
    for j in range(heigth):
        r = int(0.21*newImage[i][j][2])
        g = int(0.72*newImage [i][j][1])
        b = int(0.07*newImage [i][j][0])

        aux = b+g+r

        newImage[i][j] = [aux,aux,aux]



for i in range((width - widthWeigths)):
    for j in range((heigth - heigthWeights)):
        for x in range(widthWeigths):
            for y in range(heigthWeights):

                r = int(img[(i+x)][(y+j)][2])
                somaR += r * matrizWeigths[x][y]


        if(weigthMatriz == 0):
            newImage[i][j][2] = 1
        else:
            somaR = int(somaR/weigthMatriz)
            #print(somaR)
            newImage[i][j] = somaR
            if(somaR < 0):
                newImage[i][j][2] = 0
            if(somaR > 255):
                newImage[i][j][2] = 255



        somaR = 0


#print(img)
cv2.imshow("Face", newImage)
cv2.waitKey(0)