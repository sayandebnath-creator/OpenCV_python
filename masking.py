import cv2 as cv
import numpy as np

img = cv.imread('Photos/people.jpg') 

# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos (resolution)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img, scale=.2)
cv.imshow('Image Resized', resized_image)


blank = np.zeros(resized_image.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (resized_image.shape[1]//2 + 45,resized_image.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', mask)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)


weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)



masked = cv.bitwise_and(resized_image,resized_image,mask=weird_shape)
cv.imshow('Weired shape masked image', masked)



cv.waitKey(0)