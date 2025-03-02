import cv2 as cv
import numpy as np

img = cv.imread('Photos/girl.jpg')

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos (resolution)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img, scale=.2)
cv.imshow('Image Resized', resized_image)

blank = np.zeros(resized_image.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny= cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)
 

contours, heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')


cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank )

cv.waitKey(0)