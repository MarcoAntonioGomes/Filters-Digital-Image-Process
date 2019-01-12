import cv2
import numpy as np

img = cv2.imread('imgvin.jpg')

px = img[100,100] #BGR Color Plot B = Azul, G = Green, R = Red

print(px)

# acessing only blue pixel

blue = img[100,100,0]
print(blue)

width = img.shape[0]
print(width)

heigth = img.shape[1]
print(heigth)




for  i in range(width):
    for j in range(heigth):
        r = int(0.21*img[i][j][2])
        g = int(0.72*img [i][j][1])
        b = int(0.07*img [i][j][0])

        aux = b+g+r

        img[i][j] = [aux,aux,aux]



'''for  i in range(width):
    for j in range(heigth):
        img[i][j] = [0,0,255]
'''

cv2.imshow("Face",img)
cv2.waitKey(0)