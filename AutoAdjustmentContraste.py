import cv2
import numpy as np

img = cv2.imread('imgvin.jpg')

cv2.imshow("Teste", img)


width = img.shape[0]
print(width)

heigth = img.shape[1]
print(heigth)

aMin = 0
aMax = 155

#aH1 = maior valor de pixel na imagem
#aLo =  menor valor de pixel na imagem
aloR = img[0][0][2]
ahiR = img[0][0][2]
aloG = img[0][0][1]
ahiG = img[0][0][1]
aloB = img[0][0][0]
ahiB = img[0][0][0]

for i in range(width):
    for j in range(heigth):


        if(img[i][j][2] > ahiR):
            ahiR = img[i][j][2]
        if (img[i][j][2] < aloR):
            aloR = img[i][j][2]

        if (img[i][j][1] > ahiG):
            ahiG = img[i][j][1]
        if (img[i][j][1] < aloG):
            aloG = img[i][j][1]

        if (img[i][j][0] > ahiB):
            ahiB = img[i][j][0]
        if (img[i][j][0] < aloB):
            aloB = img[i][j][0]


for i in range(width):
    for j in range(heigth):

       r = 0 if (ahiR-aloR) == 0 else  aMin + ((int(img[i][j][2])-aloR)*((aMax-aMin)/(ahiR-aloR)))
       g = 0 if (ahiG-aloG) == 0 else aMin + ((int(img[i][j][1])-aloG)*((aMax-aMin)/(ahiG-aloG)))
       b = 0 if (ahiB-aloB) == 0 else aMin + ((int(img[i][j][0])-aloB)*((aMax-aMin)/(ahiB-aloB)))


       img[i][j] = [b,g,r]


cv2.imshow("Face", img)
cv2.waitKey(0)