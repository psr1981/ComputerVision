import cv2
import numpy as np

img = cv2.imread('images/circles.png',1);
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([169, 100, 100], dtype=np.uint8)
upper_red = np.array([189, 255, 255], dtype=np.uint8)

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img,img, mask=mask)

cv2.imshow('img', img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()
