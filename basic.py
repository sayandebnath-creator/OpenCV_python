import cv2 as cv
# bgr images
img = cv.imread('Photos/cat2.jpg') 

# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos (resolution)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img, scale=.2)
cv.imshow('Image Resized', resized_image)


# Converting to grayscale
# gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# Blur an Image
# blur = cv.GaussianBlur(resized_image, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(resized_image, 125,175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(resized_image, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
cropped = resized_image[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)