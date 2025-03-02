import cv2 as cv
import matplotlib.pyplot as plt
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

blank = np.zeros(resized_image.shape[:2], dtype='uint8')

# gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

mask = cv.circle(blank, (resized_image.shape[1]//2,resized_image.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(resized_image,resized_image,mask=mask)
cv.imshow('Mask', masked)

# # Grayscale historgram
# gray_hist = cv.calcHist([gray], [0], mask,[256],[0,256] )

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Color histogram

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([masked], [i], mask, [256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()



cv.waitKey(0)