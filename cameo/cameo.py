import cv2
import filters
from managers import WindowManager, CaptureManager
import depth

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo',
                                            self.onKeypress)
        self._captureManager = CaptureManager(
            cv2.VideoCapture(0), self._windowManager, True)
        # self._curveFilter = filters.BGRPortraCurveFilter()
        self._curveFilter = filters.SharpenFilter()
        
    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            if frame is not None:
                filters.strokeEdges(frame, frame)
                self._curveFilter.apply(frame, frame)
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """Handle a keypress.
        space -> Take a screenshot
        tab -> State/stop recording a screencast
        escape -> Quit
        """
        if keycode == 32: # scape
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo(
                    'screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
            self._windowManager.destroyWindow()

# Cameo subclass
class CameoDepth(Cameo):
    def __init__(self):
        self._windowManager = WindowManager('Cameo',
                                            self.onKeypress)
        # device = cv2.CAP_OPENNI2 # uncomment for kinect 
        device = cv2.CAP_OPENNI2_ASUS # uncomment for Xtion or Structure
        self._captureManager = CaptureManager(
            cv2.VideoCapture(device), self._windowManager, True)
        self._curveFilter = filters.BGRPortraCurveFilter()

    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            self._captureManager.channel = cv2.CAP_OPENNI_DISPARITY_MAP
            disparityMap = self._captureManager.frame
            self._captureManager.channel = cv2.CAP_OPENNI_VALID_DEPTH_MASK
            validDepthMask = self._captureManager.frame
            self._captureManager.channel = cv2.CAP_OPENNI_BGR_IMAGE
            frame = self._captureManager.frame
            if frame is None:
                # Failed to capture a BGR frame.
                # Try to capture an infrared frame instead.
                self._captureManager.channel = cv2.CAP_OPENNI_IR_IMAGE
                frame = self._captureManager.frame

            if frame is not None:
                # Make everything except the median layer black.
                mask = depth.createMedianMask(disparityMap, validDepthMask)
                frame[mask == 0] = 0

                if self._captureManager.channel == \
                   cv2.CAP_OPENNI_BGR_IMAGE:
                    # A BGR frame was captured.
                    # Apply filters to it.
                    filters.strokeEdges(frame, frame)
                    self._curveFilter.apply(frame, frame)

            self._captureManager.exitFrame()
            self._windowManager.processEvents()
                
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__=="__main__":
    Cameo().run()# uncomment for ordinary camera
    # CameoDepth().run() # uncomment for depth camera
