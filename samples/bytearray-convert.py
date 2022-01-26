import cv2
import numpy
import os

# Make an array of 120000 random bytes
qntBytes = 120000
randomByteArray = bytearray(os.urandom(qntBytes))
flatNumpyArray = numpy.array(randomByteArray)

# Convert the array to make a 400x300 grayscale image
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('RandomGray.png', grayImage) # 120,6 kB

# Convert the array to make a 400x100 color image
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('RandomColor.png', bgrImage) # 120,4 kB
