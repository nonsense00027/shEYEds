import cv2
import numpy as np
cap = cv2.VideoCapture("sample2.mp4")

while True:
    ret, frame = cap.read()
    if ret is False:
        break

scene = frame
cv2.imshow("test", scene)