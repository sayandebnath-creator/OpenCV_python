import cv2 as cv
import numpy as np

img = cv.imread('Photos/bigcat.jpg') 


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos (resolution)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img, scale=.2)
cv.imshow('Image Resized', resized_image)


gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel (used a lot)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

combine_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)

cv.imshow('Combined Sobel', combine_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)