import cv2 as cv

img = cv.imread('Photos/forest.jpg') 

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos (resolution)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img, scale=.2)
cv.imshow('Image Resized', resized_image)

# Averaging
average = cv.blur(resized_image, (3,3))
cv.imshow('Average Blur', average)

# Gaussion Blur
gauss = cv.GaussianBlur(resized_image, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(resized_image, 7)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(resized_image, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)