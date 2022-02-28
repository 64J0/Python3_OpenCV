import cv2
import helpers

imgPath = helpers.buildPath('chess_board.png')
img = cv2.imread(imgPath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = cv2.cornerHarris(gray, 2, 23, 0.04)

# cv2.cornerHarris returns an image in floating-point format. Each value
# in this image represents a score for the corresponding pixel in the source
# image. A moderate or high score indicates that the pixel is likely to be
# a corner. Conversely, we can treat pixels with the lowest scores as non-
# corners.
# Here, we select pixels with scores that are at least 1% of the highest
# score, and we color these pixels red in the original image.
img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imshow('corners', img)
cv2.waitKey()
