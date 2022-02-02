import cv2
import numpy as np

# local module
import helpers as h

# in opencv, window is draw (or re-draw) only when you call another
# function, waitKey().

imgPath = h.buildPath('github.png')
img = cv2.imread(imgPath)
cv2.imshow('github profile', img)
cv2.waitKey()
cv2.destroyAllWindows()
