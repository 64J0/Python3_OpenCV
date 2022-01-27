import cv2

# change the first pixel of an image to white - BGR
img = cv2.imread('github.png')
img[0, 0] = [255, 255, 255]

# change this other pixel in a specific position
img = cv2.imread('github.png')
img.itemset((150, 120, 0), 255) # sets the value of a pixels blue channel
img.itemset((150, 120, 1), 125) # sets the value of a pixels green channel
img.itemset((150, 120, 2), 100) # sets the value of a pixels red channel

print(img.item(150, 120, 0)) # prints the value of a pixel's blue channel
# 255
print(img.item(150, 120, 1)) # prints the value of a pixel's green channel
# 125
print(img.item(150, 120, 2)) # prints the value of a pixel's red channel
# 100

# setting all pixels green channel to 0
img = cv2.imread('github.png')
imgWithoutGreen = img[:, :, 1] = 0
# cv2.imwrite('github-without-green.png', imgWithoutGreen)

img = cv2.imread('github.png')
my_roi = img[0:100, 0:100] # ROI -> region of interest
img[300:400, 300:400] = my_roi
# cv2.imwrite('github-roi.png', img)

# numpy properties
img = cv2.imread('github.png')
print(img.shape) # (460, 460, 3) -> (height, width, n of channels)
print(img.size) # 634800 -> n of elements in the image
print(img.dtype) # uint8 -> datatype of the array
