import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import interactive
import math

# def drawRectangle(scene, grid):
#     if grid==1:
#         cv2.rectangle(scene, (0, 0), ((428), (240)), (255, 0, 0), 1)
#         aoi[0]+=1
#         gridPlot.append(1)
#     elif grid==2:
#         cv2.rectangle(scene, (428, 0), ((855), (240)), (255, 0, 0), 1)
#         aoi[1]+=1
#         gridPlot.append(2)
#     elif grid==3:
#         cv2.rectangle(scene, (856, 0), ((1280), (240)), (255, 0, 0), )
#         aoi[2]+=1
#         gridPlot.append(3)
#     elif grid==4:
#         cv2.rectangle(scene, (0, 241), ((428), (481)), (255, 0, 0), 1)
#         aoi[3]+=1
#         gridPlot.append(4)
#     elif grid==5:
#         cv2.rectangle(scene, (428, 241), ((855), (481)), (255, 0, 0), 1)
#         aoi[4]+=1
#         gridPlot.append(5)
#     elif grid==6:
#         cv2.rectangle(scene, (856, 241), ((1280), (481)), (255, 0, 0), 1)
#         aoi[5]+=1
#         gridPlot.append(6)
#     elif grid==7:
#         cv2.rectangle(scene, (0, 482), ((428), (720)), (255, 0, 0), 1)
#         aoi[6]+=1
#         gridPlot.append(7)
#     elif grid==8:
#         cv2.rectangle(scene, (428, 482), ((855), (720)), (255, 0, 0), 1)
#         aoi[7]+=1
#         gridPlot.append(8)
#     elif grid==9:
#         cv2.rectangle(scene, (856, 482), ((1280), (720)), (255, 0, 0), 1)
#         aoi[8]+=1
#         gridPlot.append(9)

def forHeatmap(x, y):
    heatmapGrid = []
    heatmapGrid.append(math.floor(x))
    heatmapGrid.append(math.floor(y))
    heatmap_array.append(heatmapGrid)

def drawRectangle(scene, grid):
    aoi[grid-1]+=1
    gridPlot.append(grid)
    xgrid_offset = xMaximumGrid[0]/2
    ygrid_offset = yMaximumGrid[0]/2
    x = 0
    y = 0
    if grid==1:
        x = math.floor(xMaximumGrid[0])
        y = math.floor(yMaximumGrid[0])
        cv2.rectangle(scene, (0, 0), (x, y), (255, 0, 0), 1)
        # print(x-xgrid_offset,y-ygrid_offset)
    elif grid==2:
        x = math.floor(xMaximumGrid[1])
        y = math.floor(yMaximumGrid[0])
        cv2.rectangle(scene, (math.floor(xMaximumGrid[0]), 0), (x, y), (255, 0, 0), 1)
    elif grid==3:
        x = math.floor(xMaximumGrid[2])
        y = math.floor(yMaximumGrid[0])
        cv2.rectangle(scene, (math.floor(xMaximumGrid[1]), 0), (x, y), (255, 0, 0), )
    elif grid==4:
        x = math.floor(xMaximumGrid[0])
        y = math.floor(yMaximumGrid[1])
        cv2.rectangle(scene, (0, math.floor(yMaximumGrid[0])), (x, y), (255, 0, 0), 1)
    elif grid==5:
        x = math.floor(xMaximumGrid[1])
        y = math.floor(yMaximumGrid[1])
        cv2.rectangle(scene, (math.floor(xMaximumGrid[0]), math.floor(yMaximumGrid[0])), (x, y), (255, 0, 0), 1)
    elif grid==6:
        x = math.floor(xMaximumGrid[2])
        y = math.floor(yMaximumGrid[1])
        cv2.rectangle(scene, (math.floor(xMaximumGrid[1]), math.floor(yMaximumGrid[0])), (x, y), (255, 0, 0), 1)
    elif grid==7:
        x = math.floor(xMaximumGrid[0])
        y = math.floor(yMaximumGrid[2])
        cv2.rectangle(scene, (0, math.floor(yMaximumGrid[1])), (x, y), (255, 0, 0), 1)
    elif grid==8:
        x = math.floor(xMaximumGrid[1])
        y = math.floor(yMaximumGrid[2])
        cv2.rectangle(scene, (math.floor(xMaximumGrid[0]), math.floor(yMaximumGrid[1])), (x, y), (255, 0, 0), 1)
    elif grid==9:
        x = math.floor(xMaximumGrid[2])
        y = math.floor(yMaximumGrid[2])
        cv2.rectangle(scene, (math.floor(xMaximumGrid[1]), math.floor(yMaximumGrid[1])), (x, y), (255, 0, 0), 1)
    
    forHeatmap(x-xgrid_offset,y-ygrid_offset)


def drawOverlay(scene):

    grid1 = cv2.rectangle(scene, (0, 0), (428,240), (0, 0, 0), -1)
    cv2.addWeighted(grid1, 0.6, scene, 0.4, 0, scene)

    # cv2.rectangle(overlay, (0, 0), (428,240), (0, 0, 0), -1)
    # cv2.addWeighted(overlay, alpha[0], scene, 1 - alpha[0], 0, scene)

    # cv2.rectangle(overlay[1], (428, 0), (855, 240), (0, 0, 0), -1)
    # cv2.addWeighted(overlay[1], alpha[1], scene, 1 - alpha[1], 0, scene)

    # cv2.rectangle(overlay, (856, 0), (1280, 240), (0, 0, 0), -1)
    # cv2.addWeighted(overlay, alpha[2], scene, 1 - alpha[2], 0, scene)

    # cv2.rectangle(overlay, (0, 241), (428, 481), (0, 0, 0), -1)
    # cv2.addWeighted(overlay, alpha[3], scene, 1 - alpha[3], 0, scene)

    # cv2.rectangle(overlay, (428, 241), (855, 481), (0, 0, 0), -1)
    # cv2.addWeighted(overlay, alpha[4], scene, 1 - alpha[4], 0, scene)

    # cv2.rectangle(overlay, (856, 241), (1280, 481), (0, 0, 0), -1)
    # cv2.addWeighted(overlay, alpha[5], scene, 1 - alpha[5], 0, scene)

    # cv2.rectangle(overlay, (0, 482), (428, 720), (0, 0, 0), -1)
    # cv2.addWeighted(overlay, alpha[6], scene, 1 - alpha[6], 0, scene)

    # cv2.rectangle(overlay, (428, 482), (855, 720), (0, 0, 0), -1)
    # cv2.addWeighted(overlay, alpha[7], scene, 1 - alpha[7], 0, scene)

    # cv2.rectangle(overlay, (856, 482), (1280, 720), (0, 0, 0), -1)
    # cv2.addWeighted(overlay, alpha[8], scene, 1 - alpha[8], 0, scene)


def updateGrid(grid):
    # global alpha
    if(grid==1 and alpha[0]>0):
        alpha[0]-=0.02
    
    # elif(grid==2 and alpha[1]>0):
    #     alpha[1]-=0.02

    # elif(grid==3 and alpha[2]>0):
    #     alpha[2]-=0.02
    
    # elif(grid==3 and alpha[2]>0):
    #     alpha[2]-=0.02

    # elif(grid==4 and alpha[3]>0):
    #     alpha[3]-=0.02

    # elif(grid==5 and alpha[4]>0):
    #     alpha[4]-=0.02

    # elif(grid==6 and alpha[5]>0):
    #     alpha[5]-=0.02

    # elif(grid==7 and alpha[6]>0):
    #     alpha[6]-=0.02

    # elif(grid==8 and alpha[7]>0):
    #     alpha[7]-=0.02

    # elif(grid==9 and alpha[8]>0):
    #     alpha[8]-=0.02


def drawChecker(scene, x1, y1, x2, y2):
    grid = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    drawRectangle(scene, grid)
    updateGrid(grid)

# CALIBRATE GAZE ON GRID SIZE DEPENDING ON INPUT VIDEO SIZE
def calibrate(point1,point2,point3,point4,point5,point6,point7,point8,point9):
    xMaximum[0] = (point1[0]+point2[0])/2
    xMaximum[1] = (point2[0]+point3[0])/2
    xMaximum[2] = point3[0] + (xMaximum[1]- point2[0])

    xMinimum = point1[0] - (xMaximum[1]- point2[0])

    yMaximum[0] = (point1[1]+point4[1])/2
    yMaximum[1] = (point4[1]+point7[1])/2
    yMaximum[0] = point7[1] + (yMaximum[1]- point4[1])

    yMinimum = point1[1] - (yMaximum[1]- point4[1])

# CALIBRATE GRID SIZE DEPENDING ON INPUT VIDEO SIZE
def calibrateGrid(width, height):
    # x-axis
    gridOffset = width/3
    # xMaximumGrid[0] = gridOffset
    # xMaximumGrid[1] = xMaximumGrid[0]+gridOffset
    # xMaximumGrid[2] = xMaximumGrid[1]+gridOffset
    xMaximumGrid.append(gridOffset)
    xMaximumGrid.append(xMaximumGrid[0]+gridOffset)
    xMaximumGrid.append(xMaximumGrid[1]+gridOffset)

    # y-axis
    gridOffset2 = height/3
    # yMaximumGrid[0] = gridOffset2
    # yMaximumGrid[1] = yMaximumGrid[0]+gridOffset2
    # yMaximumGrid[2] = yMaximumGrid[1]+gridOffset2
    yMaximumGrid.append(gridOffset2)
    yMaximumGrid.append(yMaximumGrid[0]+gridOffset2)
    yMaximumGrid.append(yMaximumGrid[1]+gridOffset2)

def plotGrid():
    # x = gridPlot
    # print(x)
    # y = gridPlot
    # print(y)
    plt.figure(1)
    plt.plot(gridPlot)
    plt.xlabel('grid')
    plt.ylabel('grid')
    plt.title('Grid Graph')
    interactive(True)
    plt.show()

    plt.figure(2)
    index = np.arange(len(gridLabel))
    # import seaborn as sns
    plt.bar(index, aoi)
    plt.xlabel('Grids', fontsize=5)
    plt.ylabel('Number of Gaze', fontsize=5)
    plt.xticks(index, gridLabel, fontsize=5, rotation=30)
    plt.title('Area of Interest')
    plt.show()

    plt.figure(3)
    plt.pie(aoi, labels=gridLabel, autopct='%1.1f%%', shadow=True, startangle=90)
    interactive(False)
    plt.show()

# def plotGridBar():
#     # this is for plotting purpose
#     index = np.arange(len(gridLabel))
#     plt.bar(index, aoi)
#     plt.xlabel('Grids', fontsize=5)
#     plt.ylabel('Number of Gaze', fontsize=5)
#     plt.xticks(index, gridLabel, fontsize=5, rotation=30)
#     plt.title('Area of Interest')
#     plt.show()


# VARIABLES..
alpha = [0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9]

aoi = [0,0,0,0,0,0,0,0,0]
gridLabel = ['Grid 1','Grid 2','Grid 3','Grid 4','Grid 5','Grid 6','Grid 7','Grid 8','Grid 9']

# x-axis maximum[current maximum]
xMaximum = []
yMaximum = []
xMinimum = 0
yMinimum = 0

xMaximumGrid = []
yMaximumGrid = []

gridPlot = []
heatmap_array = []
heatmap_list = []