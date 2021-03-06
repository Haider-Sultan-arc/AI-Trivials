import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # VideoCapture captures the video, its arguments are Camera Index number (Simply the number of camera to be used, out of all connected ones) or name of Video file

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()  # cv2.VideoCapture().read(),  read() method reads the Video we are Capturing, it returns True in case of Correctly capturing of Video and False otherwise

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release() # cv2.VideoCapture().release()
cv2.destroyAllWindows()