import cv2 as cv
import numpy as np

img = cv.imread('Photos/land.jpg')
# cv.imshow('Street', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos (resolution)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img, scale=.1)
cv.imshow('Image Resized', resized_image)

blank = np.zeros(resized_image.shape[:2], dtype='uint8')

b,g,r = cv.split(resized_image)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(resized_image.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merge = cv.merge([b,g,r])
cv.imshow('Merged Image', merge)

cv.waitKey(0)