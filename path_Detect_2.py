import cv2
import numpy as np

def empty(a):
    pass

#slider track bar creating
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",(640,240))
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("val Min","TrackBars",0,255,empty)
cv2.createTrackbar("val Max","TrackBars",255,255,empty)

hsvVals = [0,179,132,255,0,255]

def thresholding(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([hsvVals[0], hsvVals[2], hsvVals[4]])
    upper = np.array([hsvVals[1], hsvVals[3], hsvVals[5]])
    mask = cv2.inRange(hsv, lower, upper)
    # print(mask)

    return mask

def getContours(imgThres, img):

    cx = 0

    contours, hieracrhy = cv2.findContours(imgThres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:

        biggest = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(biggest)

        cx = x + w // 2

        cy = y + h // 2
        cv2.drawContours(img, biggest, -1, (255, 0, 255), 7)
        cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
        
    
        # print(x,y,w,h)

    return cx

while True:
    img = cv2.imread('E:/downloads/Picsart_24-08-28_10-32-17-097.jpg')
    img = cv2.resize(img,(640,480))
    imgThres = thresholding(img)
    cx = getContours(imgThres, img)
    imgResult = cv2.bitwise_and(img,img,mask=imgThres)
    
    
    cv2.imshow("Original",imgThres)
    cv2.imshow("detection",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break