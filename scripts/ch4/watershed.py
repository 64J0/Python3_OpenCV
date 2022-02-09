import numpy as np
import cv2
from matplotlib import pyplot as plt
import helpers

imgPath = helpers.buildPath('5_of_diamonds.png')
img = cv2.imread(imgPath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# divide the image into two regions, black and white
ret, thresh = cv2.threshold(gray, 0, 255,
                            cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# remove noise by applying a morphological transformation
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel,
                           iterations = 2)

# find the sure background region
sure_bg = cv2.dilate(opening, kernel, iterations = 3)

# find the sure foreground region
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(
    dist_transform, 0.7 * dist_transform.max(), 255, 0)
sure_fg = sure_fg.astype(np.uint8)

# find the unknown region
unknown = cv2.subtract(sure_bg, sure_fg)

# label the foreground objects
ret, markers = cv2.connectedComponents(sure_fg)

# add one to all labels so that sure background is not 0, but 1
markers += 1

# label the unknown region as 0
markers[unknown == 255] = 0

markers = cv2.watershed(img, markers)
img[markers == -1] = [255, 0, 0]

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
