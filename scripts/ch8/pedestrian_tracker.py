# The nature of the Kalman filter provides the main rationale for
# creating a Pedestrian class. The Kalman filter can predict the position
# of an object based on historical observations and can correct the
# prediction based on the actual data, but it can only do this for
# one object. As a consequence, we need one Kalman filter per object
# tracked.

import cv2
import numpy as np
import helpers

class Pedestrian():
    """A tracked pedestrian with a state including an ID, tracking
    window, histogram, and Kalman filter.
    """
    def __init__(self, id, hsv_frame, track_window):
        self.id = id
        self.track_window = track_window
        self.term_crit = \
            (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 10, 1)

        # Initialize the histogram.
        x, y, w, h = track_window
        roi = hsv_frame[y:y+h, x:x+w]
        roi_hist = cv2.calcHist([roi], [0], None, [16], [0, 180])
        self.roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255,
                                      cv2.NORM_MINMAX)

        # Initialize the Kalman filter.
        self.kalman = cv2.KalmanFilter(4, 2)
        self.kalman.measurementMatrix = np.array(
            [[1, 0, 0, 0],
             [0, 1, 0, 0]], np.float32)
        self.kalman.transitionMatrix = np.array(
            [[1, 0, 1, 0],
             [0, 1, 0, 1],
             [0, 0, 1, 0],
             [0, 0, 0, 1]], np.float32)
        self.kalman.processNoiseCov = np.array(
            [[1, 0, 0, 0],
             [0, 1, 0, 1],
             [0, 0, 1, 0],
             [0, 0, 0, 1]], np.float32) * 0.03
        cx = x + w/2
        cy = y + h/2
        self.kalman.statePre = np.array(
            [[cx], [cy], [0], [0]], np.float32)
        self.kalman.statePost = np.array(
            [[cx], [cy], [0], [0]], np.float32)

    def update(self, frame, hsv_frame):
        back_proj = cv2.calcBackProject(
            [hsv_frame], [0], self.roi_hist, [0, 180], 1)
        ret, self.track_window = cv2.meanShift(
            back_proj, self.track_window, self.term_crit)
        x, y, w, h = self.track_window
        center = np.array([x+w/2, y+h/2], np.float32)

        prediction = self.kalman.predict()
        estimate = self.kalman.correct(center)
        center_offset = estimate[:,0][:2] - center
        self.track_window = (x + int(center_offset[0]),
                             y + int(center_offset[1]), w, h)
        x, y, w, h = self.track_window

        # Draw the predicted center position as a circle.
        cv2.circle(frame, (int(prediction[0]), int(prediction[1])),
                   4, (255, 0, 0), -1)

        # Draw the corrected tracking window as a rectangle.
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)

        # Draw the ID avoce the rectangle.
        cv2.putText(frame, 'ID: %d' % self.id, (x, y-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0),
                    1, cv2.LINE_AA)

def main():
    capPath = helpers.buildPath('pedestrians.avi')
    cap = cv2.VideoCapture(capPath)
    
    # Create the KNN background subtractor.
    bg_subtractor = cv2.createBackgroundSubtractorKNN()
    history_length = 20
    bg_subtractor.setHistory(history_length)
    
    erode_kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE, (3, 3))
    dilate_kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE, (8, 3))
    
    pedestrians = []
    num_history_frames_populated = 0
    
    while True:
        grabbed, frame = cap.read()
        if (grabbed is False):
            break
        
        # Apply the KNN background subtractor
        fg_mask = bg_subtractor.apply(frame)
        
        # Let the background subtractor build up a history.
        if num_history_frames_populated < history_length:
            num_history_frames_populated += 1
            continue
        
        # Create the thresholded image.
        _, thresh = cv2.threshold(fg_mask, 127, 255,
                                  cv2.THRESH_BINARY)
        cv2.erode(thresh, erode_kernel, thresh, iterations=2)
        cv2.dilate(thresh, dilate_kernel, thresh, iterations=2)
        
        # Detect contours in the thresholded image.
        contours, hier = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Draw rectangles around large contours.
        # Also, if no pedestrians are being tracked yet, create some.
        should_initialize_pedestrians = len(pedestrians) == 0
        id = 0
        for c in contours:
            if cv2.contourArea(c) > 500:
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x+w, y+h),
                              (0, 255, 0), 1)
                if should_initialize_pedestrians:
                    pedestrians.append(
                        Pedestrian(id, hsv_frame,
                                   (x, y, w, h)))
                    id += 1
                    
        # Update the tracking of each pedestrian.
        for pedestrian in pedestrians:
            pedestrian.update(frame, hsv_frame)
            
        cv2.imshow('Pedestrians Tracked', frame)

        k = cv2.waitKey(110)
        if k == 27: # Escape
            break

if __name__ == "__main__":
    main()
