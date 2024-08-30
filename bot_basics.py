import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        
        if area > 500:
            cv2.drawContours(imgCounter,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(approx)
            print(len(approx))
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            
            if objCor == 3: objectType = 'Tri'
            elif objCor == 4:
                aspratio = w/float(h)
                if aspratio > 0.95 and aspratio < 1.05 : objectType = 'square'
                else: objectType = 'rectangle'
            elif objCor > 4: objectType = 'Circle'
            else: objectType ='None'
            cv2.rectangle(imgCounter,(x,y),(x+w,y+h),(250,0,200),2)
            cv2.putText(imgCounter,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)
            


img = cv2.imread("E:/downloads/Picsart_24-08-28_10-32-17-097.jpg")
imgCounter = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)

getContours(imgCanny)
imgBlank = np.zeros_like(img)



cv2.imshow("Track",imgBlank)
cv2.waitKey(0)
cv2.destroyAllWindows()