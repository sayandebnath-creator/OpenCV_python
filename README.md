# OpenCV with Python in 4 Hours
Notes and code used in my [**Python and OpenCV course**](https://youtu.be/oXlwWbU8l2o). You can find me on [Twitter](https://twitter.com/jasmcaus) for more info on courses I'm working on currently.


## Important Updates:
`caer.train_val_split()` is a deprecated feature in [`caer`](https://github.com/jasmcaus/caer/). Use `sklearn.model_selection.train_test_split()` instead. See [#9](https://github.com/jasmcaus/opencv-course/issues/9) for more details.


# Course Outline (with timestamps)
## 1. Installation
Besides installing OpenCV, we cover the installation of the following package:

[**`Caer`**](https://github.com/jasmcaus/caer/) is a *lightweight, high-performance* Vision library for high-performance AI research. It simplifies your approach towards Computer Vision by abstracting away unnecessary boilerplate code giving you the **flexibility** to quickly prototype deep learning models and research ideas. 
```bash
$ pip install caer
```


## 2. Basic Concepts:
- Reading Images and Video
- Resizing and Rescaling Images and Video Frames
- Drawing Shapes and Placing text on images
- 5 Essential Methods in OpenCV
- Image Transformations 
- Contour Detection 
    
## 3. Advanced Concepts:
- Switching between Colour Spaces (RGB, BGR, Grayscale, HSV and L*a*b)
- Splitting and Merging Colour Channels
- Blurring 
- BITWISE operations
- Masking 
- Histogram Computation
- Thresholding/Binarizing Images
- Advanced Edge Detection
    
## 4. Face Detection and Recognition
- Face Detection using Haar Cascades
- Face Recognition using OpenCV's LBPHFaceRecognizer algorithm 
