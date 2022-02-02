import cv2

# local module
import helpers as h

# returns an image in the BGR color format even
# if the file uses a grayscale format.
exampleImagePath = h.buildPath('github.png')
image = cv2.imread(exampleImagePath) # 2,8 kB

jpgExampleImagePath = h.buildPath('github.jpg')
cv2.imwrite(jpgExampleImagePath, image) # 34,6 kB

grayImage = cv2.imread(exampleImagePath, cv2.IMREAD_GRAYSCALE)
grayExampleImagePath = h.buildPath('github-gray.png')
cv2.imwrite(grayExampleImagePath, grayImage) # 8,9 kB
