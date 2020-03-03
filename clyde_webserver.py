#!/usr/bin/env python
import cv2
import numpy as np
from flask import Flask, render_template, Response
from clyde_video import Video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(video):
    
    while True:
        frame = video.get_frame()
        # ret, frame = cap.read()

        # roi = frame[269: 795, 537: 1416]
        roi = frame

        rows, cols, _ = roi.shape
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)

        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)

        _, threshold = cv2.threshold(gray_roi, 50, 255, cv2.THRESH_BINARY_INV)
        # _, threshold = cv2.threshold(gray_roi, 50, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
            cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
            break    

        gray_roi_3channel = cv2.cvtColor(gray_roi, cv2.COLOR_GRAY2BGR)
        threshold_3channel = cv2.cvtColor(threshold, cv2.COLOR_GRAY2BGR)
        
        numpy_horizontal_concat1 = np.concatenate((roi, threshold_3channel), axis=1)



        # # frame = numpy_horizontal_concat1
        # # print(frame)
        # gray_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)  
        # gray_roi_3channel = cv2.cvtColor(gray_roi, cv2.COLOR_GRAY2BGR)

        # frame = gray_roi_3channel
        frame = numpy_horizontal_concat1

        
        # web render
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Video()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)