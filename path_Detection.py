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


while True:
    img = cv2.imread('E:/downloads/Picsart_24-08-28_10-32-17-097.jpg')
    img = cv2.resize(img,(640,480))
    
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    # print(h_min)
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("val Min","TrackBars")
    v_max = cv2.getTrackbarPos("val Max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    
    
    cv2.imshow("Original",img)
    cv2.imshow("result",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
# For RED : ---- 0 179 132 255 0 255---