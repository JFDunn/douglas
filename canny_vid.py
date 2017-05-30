import numpy as np
import cv2
import io
import picamera
import picamera.array
camera = picamera.PiCamera()
stream = picamera.array.PiRGBArray(camera)


for foo in camera.capture_continuous(stream, format='bgr'):
    ret3,frame = cv2.threshold(cv2.bilateralFilter(cv2.cvtColor(cv2.resize(stream.array, [500,500]), cv2.COLOR_BGR2GRAY),12,70,70),0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    edges = cv2.Canny(frame,1000,1000, 5)
    lines = cv2.HoughLines(edges,1,np.pi/180,100)
    print lines[0]
#    for rho,theta in lines[0]:
#        a = np.cos(theta)
#        b = np.sin(theta)
#        x0 = a*rho
#        y0 = b*rho
#        x1 = int(x0 + 1000*(-b))
#        y1 = int(y0 + 1000*(a))
#        x2 = int(x0 - 1000*(-b))
#        y2 = int(y0 - 1000*(a))
#
#        cv2.line(color,(x1,y1),(x2,y2),(0,0,255),2)
#    cv2.imshow('Trajectory',color)

    stream.truncate()
    stream.seek(0)
