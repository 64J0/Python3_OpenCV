import cv2

WINDOW_NAME = 'MyWindow'
clicked = False

def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow(WINDOW_NAME)
cv2.setMouseCallback(WINDOW_NAME, onMouse)

print('Showing camera feed. Click window or press any key to stop.')
success, frame = cameraCapture.read()

# waitKey argument is a number of milliseconds to wait for keyboard input
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow(WINDOW_NAME, frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow(WINDOW_NAME)
cameraCapture.release()
