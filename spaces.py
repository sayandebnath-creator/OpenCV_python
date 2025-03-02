import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/street.jpg')
# cv.imshow('Street', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos (resolution)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img, scale=.1)
cv.imshow('Image Resized', resized_image)

# plt.imshow(resized_image)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(resized_image, cv.COLOR_BGR2HSV)
cv.imshow('Hsv', hsv)

# BGR to L*a*b
lab = cv.cvtColor(resized_image, cv.COLOR_BGR2LAB)
cv.imshow('Lab', lab)

# BGR to RGB
rgb = cv.cvtColor(resized_image, cv.COLOR_BGR2RGB)
cv.imshow('Rgb', rgb)

# HSV to BGR ( we can convert vice-versa)
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV---> BGR', hsv_bgr)

plt.imshow(rgb)
plt.show()



cv.waitKey(0)

