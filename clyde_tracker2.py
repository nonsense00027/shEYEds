import cv2
import numpy as np
cap = cv2.VideoCapture("eyes.mp4")
cap2 = cv2.VideoCapture("scenes.mp4")

width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
print(width, height)

centerX = 610
centerY = 340
counter = 0
while True:
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()
    if ret is False:
        break

    #frame size
    

    # roi = frame[269: 795, 537: 1416]
    roi = frame
    # roi2 = frame2[269: 795, 537: 1416]
    roi2 = frame2
    # roi = frame
    
    #mirror video
    roiINV = cv2.flip(roi,1)

    rows, cols, _ = roiINV.shape
    # gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)

    gray_roi = cv2.cvtColor(roiINV, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)
    

    _, threshold = cv2.threshold(gray_roi, 20, 255, cv2.THRESH_BINARY_INV)
    # _, contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    #middle calibration
    
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        #cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
        cv2.rectangle(roiINV, (x, y), (x + w, y + h), (255, 0, 0), 2)
        if counter==0:
            print(counter)
            print(x,y)
            print(x+w, y+h)
        xOffset = round(x*0.69)
        yOffset = round(y*2.7)
        cv2.rectangle(roi2, (xOffset, yOffset), ((xOffset + w), (yOffset + h)), (255, 0, 0), 2)
        # cv2.rectangle(roi2, (centerX, centerY), (centerX+60, centerY+40), (255, 0, 0), 2)
        cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
        cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
        counter = 1
        break    

    gray_roi_3channel = cv2.cvtColor(gray_roi, cv2.COLOR_GRAY2BGR)
    threshold_3channel = cv2.cvtColor(threshold, cv2.COLOR_GRAY2BGR)

    
    # numpy_horizontal = np.hstack((roi, gray_roi_3channel))
    # numpy_horizontal_concat = np.concatenate((roi, gray_roi_3channel), axis=0)

    # row1 = np.hstack((frame, threshold_3channel))
    # numpy_horizontal_concat1 = np.concatenate((roi, threshold_3channel), axis=1)

    # cv2.namedWindow('Threshold',cv2.WINDOW_NORMAL)
    # cv2.namedWindow('gray roi',cv2.WINDOW_NORMAL)
    # cv2.namedWindow('Roi',cv2.WINDOW_NORMAL)
    # cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    # cv2.namedWindow('Roi and Gray roi',cv2.WINDOW_NORMAL)        
    # cv2.namedWindow('1',cv2.WINDOW_NORMAL)        
    # cv2.resizeWindow('Threshold', 300,300)
    # # cv2.resizeWindow('gray roi', 300,300)
    # # cv2.resizeWindow('Roi', 300,300)
    # cv2.resizeWindow('Roi and Gray roi', 500,500)        
    # cv2.resizeWindow('1', 500,500)        
    # cv2.resizeWindow('frame', 300,300)            

    # cv2.imshow("Threshold", threshold)
    # cv2.imshow("gray roi", gray_roi)
    # cv2.imshow("Roi", roi)    
    # cv2.imshow("Roi and Gray roi", numpy_horizontal_concat)
    # cv2.imshow("1", numpy_horizontal_concat1)
    # cv2.imshow("frame", frame)

    cv2.imshow("Eyes", roiINV)
    cv2.imshow("Scene", roi2)
    key = cv2.waitKey(30)
    if key == 27:
        break

cv2.destroyAllWindows()    