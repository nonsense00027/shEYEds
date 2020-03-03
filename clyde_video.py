import cv2
import numpy as np
from time import time

class Video(object):
    def __init__(self):
        # self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]
        self.frames = []
        # self.video = cv2.VideoCapture("eye_recording.mp4")
        self.video = cv2.VideoCapture("source4.mp4")
        # self.video = cv2.VideoCapture("eye_recording.mp4")

    def get_frame(self):
        success, image = self.video.read()        
        # ret, jpeg = cv2.imencode('.jpg', image)
        # return jpeg.tobytes()
        return image