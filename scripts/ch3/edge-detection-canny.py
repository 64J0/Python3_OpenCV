import cv2
import numpy as np
import helpers


imgPath = helpers.buildPath("github.jpg")
# cv2.IMREAD_GRAYSCALE = 0
img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

dstImgPath = helpers.buildPath("canny.jpg")
cv2.imwrite(dstImgPath, cv2.Canny(img, 200, 300)) # Canny in one line!
cv2.imshow("canny", cv2.imread(dstImgPath))
cv2.waitKey()
cv2.destroyAllWindows()
