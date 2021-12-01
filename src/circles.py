import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def circles(img):
    img = cv.imread(img,0)
    img = cv.medianBlur(img,5)

    
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)


    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,2,65,
                            param1=600,param2=70,minRadius=0,maxRadius=0)

    circles = np.uint64(np.around(circles))

    for c in circles[0,:]:
        
        cv.circle(cimg,(c[0],c[1]),c[2],(0,225,0),2)
        cv.circle(cimg,(c[0],c[1]),2,(0,0,255),3)
        
        
    cv.imshow("detected circles",cimg)

    cv.waitKey(0)
    cv.destroyAllWindows()
