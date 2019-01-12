import cv2
import numpy as np

img = cv2.imread('imgvin.jpg')

px = img[100, 100]  # BGR Color Plot B = Azul, G = Green, R = Red

print(px)

# acessing only blue pixel

blue = img[100, 100, 0]
print(blue)

width = img.shape[0]
print(width)

heigth = img.shape[1]
print(heigth)

valor = 100
for i in range(width):
    for j in range(heigth):
        r = int(img[i][j][2]) + valor
        g = int(img[i][j][1])  + valor
        b = int(img[i][j][0]) + valor



        r = 255 if r > 255 else r
        g = 255 if g > 255 else g
        b = 255 if b > 255 else b

        img[i][j] = [b,g,r]

'''for i in range(width):
    for j in range(heigth):
        if (img[i][j][0] < trash):
            img[i][j] = 0

        else:
            img[i][j] = 255
'''

cv2.imshow("Face", img)
cv2.waitKey(0)