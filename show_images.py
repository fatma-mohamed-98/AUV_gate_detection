import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img,imgContour):
    retrieval_mod = cv2.RETR_EXTERNAL
    contours, hierarchy = cv2.findContours(img, retrieval_mod, cv2.CHAIN_APPROX_NONE)


    x_arr = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >1000:
            cv2.drawContours(imgContour, cnt, -1, (0,255, 100),10)
#========== to get the number of corners in each shape to detect the type of the detected shape =======================
            closed = True
            resolution = 0.02
            curveLength = cv2.arcLength(cnt, closed)
            approx_corner_points = cv2.approxPolyDP(cnt, resolution * curveLength, closed)
            Num_objCorners = len(approx_corner_points)
            x, y, w, h = cv2.boundingRect(approx_corner_points)
            print(x, y, w, h )
            x_arr.append(x)

            if Num_objCorners >2 and Num_objCorners <7:
                cv2.rectangle(imgContour, (x, y), (x + w, y + h), (200, 100, 255), 7)
            # objectType = 'gate'



            # cv2.rectangle(imgContour, (x, y), (x + w, y + h), (200, 100, 255), 7)
            # cv2.putText(imgContour, objectType,
            #             (x + (w // 2)-10 , y + (h // 2) ), cv2.FONT_HERSHEY_COMPLEX, 2,
            #             (0, 0, 0), 5)


    print(min(x_arr))