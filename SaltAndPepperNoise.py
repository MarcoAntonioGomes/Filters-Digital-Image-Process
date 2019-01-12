from skimage import novice
from skimage import data
import numpy as np
import math
from skimage.novice import Picture
import random

img = novice.open('sobel.png')

print(img.size)
width = img.width
height = img.height

noiseAmount = 10;

noise = int((width*height*noiseAmount) / 200);

def SaltAndPepperNoise(noiseAmount):
  return max(0, min(100, noiseAmount))


for i in range(noise):
             x = random.randint(0,(width-1))
             y = random.randint(0,(height-1))


             band = random.randint(0,1);
             color = random.randint(0,1);
             c = [0,255]

             if(band == 0):
                img[x,y].red = c[color]

             elif(band == 1):
                img[x, y].green = c[color]

             elif(band == 2):
                img[x, y].blue = c[color]




img.show()
