import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('village.png',0)#that why original is gray already
img=cv.resize(img, (300,300))
_,th1=cv.threshold(img, 100, 255, cv.THRESH_BINARY) #try to change value of second and third argument to get best result
_,th2=cv.threshold(img,100,255,cv.THRESH_BINARY_INV)
_,th3=cv.threshold(img,130,255,cv.THRESH_TRUNC)
_,th4=cv.threshold(img,150,255,cv.THRESH_TOZERO)
_,th5=cv.threshold(img,100,255,cv.THRESH_TOZERO_INV)
#now lets show all the window using matplotlib
titles=['original','THRESH_BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
images=[img,th1,th2,th3,th4,th5]#there are 6 image
#so lets use a loop which iterate 6 times
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
