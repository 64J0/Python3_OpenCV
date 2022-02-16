import cv2
import helpers

frontalfacepath = helpers.buildPath('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(frontalfacepath)

imgPath = helpers.buildPath('woodcutters.jpg')
img = cv2.imread(imgPath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.08, 5)
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.namedWindow('Woodcutters detected!')
cv2.imshow('Woodcutters detected!', img)

resultPath = helpers.buildPath('woodcutters_detected.jpg')
cv2.imwrite(resultPath, img)
cv2.waitKey(0)
