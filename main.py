
import cv2
import sys
import mediapipe as mp

# TODO: implement a safer, effective and understandable method to plot hand landmarks
# open a window in matplotlib with the hand gesture (letter in asl), with the landmarks and the annotation
# TODO: do this tmr

import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_drawing
hands = mp_hands.Hands()

# window
cam = cv2.VideoCapture(0) # idx 0
name = "asl-translator"

if not cam.isOpened():
    raise Exception("Could not open camera")

# window
cv2.namedWindow(name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(name, 640, 480) 

while cv2.getWindowProperty(name, cv2.WND_PROP_VISIBLE) > 0:
    # read a frame from the camera
    ret, frame = cam.read()

    # check if frame is read
    if not ret:
        raise Exception("[ERROR] Could not read frame from camera")
    
    # every frame, run this loop
    # draw the landmarks on the hand
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)


    if results.multi_hand_landmarks:
        for landmark in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, landmark, mp_hands.HAND_CONNECTIONS)
        
    # show the frame
    cv2.imshow(name, frame)
    # if a key was pressed and the key is "q" quit the program
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# release the camera
cam.release()
# destroy the window
cv2.destroyAllWindows()

