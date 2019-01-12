import cv2
import numpy as np

img = cv2.imread('imgvin.jpg')


width = img.shape[0]
print(width)

heigth = img.shape[1]
print(heigth)


for i in range(width):
    for j in range(heigth):
        r = int(img[i][j][2])
        g = int(img[i][j][1])
        b = int(img[i][j][0])

        r = 255 - r
        g = 255 - g
        b = 255 - b

        img[i][j] = [b,g,r]


cv2.imshow("Face", img)
cv2.waitKey(0)