import cv2
import helpers

faceCascadePath = helpers.buildPath('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(faceCascadePath)

eye_path = helpers.buildPath('haarcascade_eye.xml')
eye_cascade = cv2.CascadeClassifier(eye_path)

camera = cv2.VideoCapture(0)
while (cv2.waitKey(1) == -1):
    success, frame = camera.read()
    if success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, 1.3, 5, minSize=(120, 120))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(
                roi_gray, 1.03, 5, minSize=(40, 40))
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(frame, (x+ex, y+ey),
                              (x+ex+ew, y+ey+eh), (0, 255, 0), 2)
            cv2.imshow('Face Detection', frame)
