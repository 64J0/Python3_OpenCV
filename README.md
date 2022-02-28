# OpenCV + Python3

> Computer vision is a relatively young branch of computer science, so many famous algorithms and techniques have only been invented recently.

In this repository I'll store some codes that are developed while learning both Python 3 and OpenCV through `Learning OpenCV 4 Computer Vision with Python 3` book.

My development environment:

* Ubuntu 20.04
* Python 3.8.5

## Installation:

```shell
  $ sudo apt update
  $ sudo apt install python3-numpy python3-scipy
  $ pip install -r requirements.txt
  # ~/.pyenv/versions/3.8.5/lib/python3.8/site-packages/cv2/data
```

## Common applications:

* Photo/video editors
* Motion-controlled games
* Robot's AI
* Psuchology experiments to keep track of participants' eye movements

## Notes:

> OpenCV's Python module is called cv2 even though we are using OpenCV 4.x and not OpenCV 2.x. Historically, OpenCV had two Python modules: cv2 and cv. The latter wrapped a legacy version of OpenCV implemented in C. Nowadays, OpenCV has only the cv2 Python module, which wraps the current version of OpenCV implemented in C++.

> The numpy.array class is greatly optimized for array operations, and it allows certain kinds of bulk manipulations that are not available in a plain Python list. These kinds of numpy.array type-specific operations come in handy for image manipulations in OpenCV.

> OpenCV's implementations of the Hough transform are limited to detecting lines and circles; however, we already implicitly explored shape detection in general when we talked about approxPolyDP. This function allows for the approximation of polygons, so if your image contains polygons, they will be accurately detected through the combined use of cv2.findContours and cv2.approxPolyDP.

### Color formats:

When we apply computer vision techniques to images, we will typically work with three kinds of color models: grayscale, blue-green-red (BGR) and hue-saturation-value (HSV).

* **Grayscale** is a model that reduces color information by translating it into shades of gray or brightness. This model is extremely useful for the intermediate processing of images in problems where brightness information alone is sufficient, such as face detection. Typically, each pixel in a grayscale image is represented by a single 8-bit value, randing from 0 for black to 255 for white.
* **BGR** is the blue-green-red color model, in which each pixel has a triplet of values representing the blue, green, and red components or **channels** of the pixel's color. Web developers, and anyone who works with computer graphics, will be familiar with a similar definition of colors, except with the reverse channel order, red-green-blue (RGB). Typically, each pixel in a BGR image is represented by a triplet of 8-bit values, such as [0, 0, 0] for black, [255, 0, 0] for blue, ..., [255, 255, 255] for white.
* **HSV** model uses a different triplet of channels. Hue is the color's tone, saturation is its intensity, and value represents its brightness.

By default, OpenCV uses the BGR color model (with 8 bits per channel) to represent any image that it loads from a file or captures from a camera.

[...] The color models that are used in computing are called **additive** models and they deal with lights. Lights behave differently from paints (which follow a **subtractive** color model), and since software runs on a computer whose medium is a monitor that emits light, the color model of reference is the additive one.

## Other libraries facilities:

* **NumPy** has a fast fourier transform package, which contains the fft2 method. This method allows us to compute a discret Fourier transform (DFT) of an image. [...] The Fourier transform is the basis of many algorithms that are used for common image processing operations, such as edge detection or line and shape detection.

## Definitions:

* **Magnitude spectrum** of an image is another image that provides a representation of the original image in terms of its changes.

* **HPF** is a filter that examines a region of an image and boosts the intensity of certain pixels based on the difference in the intensity of the surrounding pixels.

* **Kernel** is a set of weights that are applied to a region in a source image to generate a single pixel in the destination image. Another term for a kernel is a **convolution matrix**. More information on [this link](https://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/).

* **Feature of an image** is an area of interest in the image that is unique or easily recognizable. **Corners** and regions with a high density of textural detail are good features, while patterns that repeat themselves a lot and low-density regions (such as a blue sky) are not. Edges are good features as they tend to divide two regions of an image. A **blob** (a region of an image that greatly differs from its surrounding areas) is also an interesting feature.

* **Scale-Invariant Feature Transform**: We need a function (a transform) that will detect features (a feature transform) and will not output different results depending on the scle of the image (a scale-invariant feature transform). Note that SIFT does not detect keypoints (which is done with the **Difference of Gaussians (DoG)**; instead, it describes the region surrounging them by means of a feature vector. 

* **FLANN** stands for **Fast Library for Approximate Nearest Neighbors**. It is an open source library under the permissive 2-clause BSD license. It is a library for performing fast approximate nearest neighbor searches in high-dimensional spaces. It contains a collection of algorithms that work best for the nearest neighbor search and a system for automatically choosing the best algorithm and optimum parameters depending on the dataset.

* **Homography** is a condition in which two figures find each other when one is a perspective distortion of the other.

* **HOG** stands for **Histogram of Oriented Gradients**. It is a feature descriptor, so it belongs to the same family of algorithms as **scale-invariant feature transform (SIFT)**, **speeded-up robust features (SURF)**, and **Oriented FAST and rotated BRIEF (ORB)**.

* **SVM** is a technique to find the plane that divides differently labeled data by the largest possible margin. https://link.springer.com/article/10.1007/BF00994018.

## Algorithms:

* **Haar cascade classifiers**: analyze the contrast between adjacent image regions to determine whether or not a given image or sub image matches a known type. In practice we generally combine Haar cascade classifiers in a hierarchy so that one classifier identifies a parent region and other classifiers identify child regions.

### Types of feature detection and matching

A number of algorithms can be used to detect and describe features, and we will explore several of them in this section. The most commonly used feature detection and descriptior extraction algorithms in OpenCV are as follows:

* **Harris**: detecting corners.
* **SIFT**: detecting blobs.
* **SURF**: detecting blobs.
* **FAST**: detecting corners.
* **BRIEF**: detecting blobs.
* **ORB**: stands for **Oriented FAST and Rotated BRIEF**. It is useful for detecting a combination of corners and blobs.

## Useful links:

* https://www.face-rec.org/databases/
* http://vision.ucsd.edu/content/yale-face-database
* http://vision.ucsd.edu/content/extended-yale-face-database-b-b
* http://www.cl.cam.ac.uk/research/dtg/attarchive/facedatabase.html
