import cv2
import numpy as np
import random
import functions as fu
import gaze_plot as ga

# drawRectangle(200,500)
cap = cv2.VideoCapture("sample.mp4")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1280,  720))

width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
print(width, height)
print(fu.alpha)

# grid = [x-axis, y-axis]
point1 = []
point2 = []
point3 = []
point4 = []
point5 = []
point6 = []
point7 = []
point8 = []
point9 = []

# fu.calibrate(point1, point2, point3, point4, point5, point6, point6, point7, point8, point9)
fu.calibrateGrid(width, height)
while True:
    ret, frame = cap.read()
    if ret == False:
        break

    # roi = frame[241:428, 481:855]
    # drawChecker(roi, 0, 0, 427, 240)
    # cv2.imshow("Scene", roi)

    scene = frame
    # overlay = frame.copy()
    # overlay = frame.copy()
    # grid1 = cv2.rectangle(scene, (0, 0), (428,240), (0, 0, 0), -1)
    # cv2.addWeighted(grid1, 1, scene, 0, 0, scene)
    # fu.drawOverlay(scene)
    fu.drawChecker(scene, 0, 0, 427, 240)

    # out.write(scene)

    cv2.imshow("Scene", scene)
    

    key = cv2.waitKey(30)
    if key == 27:
        # print(fu.aoi)
        # print(fu.alpha)
        # print(fu.gridPlot)
        # fu.plotGrid()
        # fu.plotGridBar()
        # print(fu.heatmap_array)
        # fu.heatmap_list = list(map(lambda q: (int(q[0]), int(q[1]), 1), fu.heatmap_array))
        # print(fu.heatmap_list)
        # ga.displayHeatmap(fu.heatmap_array)
        ga.displayHeatmap(fu.heatmap_array, 1280, 720, 0.6, 'sampleheatmap', 'sample.png', 200, 33)
        break

# print(fu.aoi)
# fu.plotGrid()
cv2.destroyAllWindows()