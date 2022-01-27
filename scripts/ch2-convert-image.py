import cv2

# returns an image in the BGR color format even
# if the file uses a grayscale format.
image = cv2.imread('github.png') # 2,8 kB
cv2.imwrite('github.jpg', image) # 34,6 kB

grayImage = cv2.imread('github.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('github-gray.png', grayImage) # 8,9 kB
