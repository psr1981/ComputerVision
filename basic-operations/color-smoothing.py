import cv2
import numpy as np

img = cv2.imread('images/dress.jpg');

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)

cv2.imshow('img', img)
cv2.imshow('blur',blur)
cv2.imshow('gblur',gblur)
cv2.imshow('dst',dst)


cv2.waitKey(0)
cv2.destroyAllWindows()
