import cv2
import numpy as np

# create a black square with 200 x 200
img = np.zeros((200, 200), dtype=np.uint8)

# put a white square in the middle
img[50:150, 50:150] = 255

ret, thresh = cv2.threshold(img, 127, 255, 0)

hierarchyType = cv2.RETR_TREE
contourApproximation = cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours(thresh, hierarchyType,
                                       contourApproximation)

color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
cv2.imshow("contours", color)
cv2.waitKey()
cv2.destroyAllWindows()
