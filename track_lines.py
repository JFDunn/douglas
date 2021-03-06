from numpy import array, average, pi, where
from math import degrees
from cv2 import threshold, cvtColor, resize, COLOR_BGR2GRAY, THRESH_BINARY, THRESH_OTSU, Canny, HoughLines, bilateralFilter
from picamera import PiCamera
from picamera.array import PiRGBArray
from steering import turn, kill
camera = PiCamera()
stream = PiRGBArray(camera)

half=pi/2

for foo in camera.capture_continuous(stream, format='bgr', resize=(640,480), use_video_port=True):
    ret3,frame = threshold(bilateralFilter(cvtColor(stream.array, COLOR_BGR2GRAY),12,70,70),0,255,THRESH_BINARY+THRESH_OTSU)
    edges = Canny(frame,1000,1000, 5)
    lines = HoughLines(edges,1,pi/180,100)
    if lines is None:
        kill()
        stream.truncate()
        stream.seek(0)
        continue
    thetas=array([theta for rho, theta in lines[0]])
    theta_filtered=thetas[where((thetas>=0) & (thetas <=pi))]

    #use list of thetas to figure out degrees to turn
    if (average(theta_filtered) < half):
        radians_to_turn = half - average(thetas)
        turn(degrees(radians_to_turn), dir=False)
    else:
        radians_to_turn = average(thetas) - half
        turn(degrees(radians_to_turn), dir=True)
    stream.truncate()
    stream.seek(0)
