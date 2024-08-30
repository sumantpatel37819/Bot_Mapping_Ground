import cv2
import numpy as np

def empty(a):
    pass

# slider track bar creating
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", (640, 240))
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("val Max", "TrackBars", 255, 255, empty)

# Manually set HSV values for red detection
hsvVals = [0,179,132,255,0,255]  # Adjust these values if needed

def thresholding(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([hsvVals[0], hsvVals[2], hsvVals[4]])
    upper = np.array([hsvVals[1], hsvVals[3], hsvVals[5]])
    mask = cv2.inRange(hsv, lower, upper)
    return mask

def getContours(imgThres, img):
    contours, hierarchy = cv2.findContours(imgThres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        biggest = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(biggest)
        return x, y, w, h
    return None

while True:
    img = cv2.imread('E:/downloads/Picsart_24-08-28_10-32-17-097.jpg')
    img = cv2.resize(img, (640, 480))
    imgThres = thresholding(img)
    rect = getContours(imgThres, img)
    
    if rect is not None:
        x, y, w, h = rect

        # Move the green circle from x to (x + w)
        for i in range(x, x + w):
            img = cv2.imread('E:/downloads/Picsart_24-08-28_10-32-17-097.jpg')
            img = cv2.resize(img, (640, 480))
            imgThres = thresholding(img)
            imgResult = cv2.bitwise_and(img, img, mask=imgThres)

            # Draw green circle at the current position i
            cv2.circle(img, (i, y + h // 2), 10, (0, 255, 0), cv2.FILLED)
            cv2.imshow("Original", img)
            cv2.imshow("Detection", imgResult)
            
            cv2.waitKey(10)
               

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()