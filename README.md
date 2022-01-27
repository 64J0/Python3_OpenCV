# OpenCV + Python3

In this repository I'll store some codes that are developed while learning both Python 3 and OpenCV through `Learning OpenCV 4 Computer Vision with Python 3` book.

My development environment:

* Ubuntu 20.04
* Python 3.8.5

## Installation

```shell
  $ sudo apt update
  $ sudo apt install python3-numpy python3-scipy
  $ pip install -r requirements.txt
```

## Notes

> OpenCV's Python module is called cv2 even though we are using OpenCV 4.x and not OpenCV 2.x. Historically, OpenCV had two Python modules: cv2 and cv. The latter wrapped a legacy version of OpenCV implemented in C. Nowadays, OpenCV has only the cv2 Python module, which wraps the current version of OpenCV implemented in C++.

> The numpy.array class is greatly optimized for array operations, and it allows certain kinds of bulk manipulations that are not available in a plain Python list. These kinds of numpy.array type-specific operations come in handy for image manipulations in OpenCV.
