# OpenCV + Python3

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

## Algorithms:

* **Haar cascade classifiers**: analyze the contrast between adjacent image regions to determine whether or not a given image or sub image matches a known type. In practice we generally combine Haar cascade classifiers in a hierarchy so that one classifier identifies a parent region and other classifiers identify child regions.

## Useful links:

* https://www.face-rec.org/databases/
* http://vision.ucsd.edu/content/yale-face-database
* http://vision.ucsd.edu/content/extended-yale-face-database-b-b
* http://www.cl.cam.ac.uk/research/dtg/attarchive/facedatabase.html
