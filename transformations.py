import cv2 as cv
import numpy as np


img = cv.imread('Photos/cat.jpg')

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos (resolution)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img, scale=.2)
cv.imshow('Image Resized', resized_image)


# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(resized_image, -100 , 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)
     
    return cv.warpAffine(resized_image, rotMat, dimensions)

rotated = rotate(resized_image, -45)
cv.imshow('Rotated', rotated)   


rotated_rotated = rotate(resized_image, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(resized_image, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', resized)

# Flipping (horizontally=1, vertically=-1)
flip = cv.flip(resized_image, 1)
cv.imshow('Flip', flip)

# Cropping
cropped = resized_image[200:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)