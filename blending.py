import cv2
import numpy as np

# Load the images
img1 = cv2.imread('medium.jpg')
img2 = cv2.imread('rohit.jpg')

# Resize the images to the same size
img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

# Blend the images
blended_img = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# Display the original and blended images
cv2.imshow('Original Image 1', img1)
cv2.imshow('Original Image 2', img2)
cv2.imshow('Blended Image', blended_img)
cv2.waitKey(0)
cv2.destroyAllWindows()