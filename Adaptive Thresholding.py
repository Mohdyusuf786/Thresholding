import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('village.png',0) #that why original is gray already
img=cv.resize(img, (300,300))

th1=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,12)
th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,12)

#now lets show all the window using matplotlib
titles=['original','ADAPTIVE_THRESH_MEAN_C','ADAPTIVE_THRESH_GAUSSIAN_C']
images=[img,th1,th2] #there are 3 image
for i in range(3):
    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
