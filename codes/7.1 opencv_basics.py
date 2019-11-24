import cv2

camera=cv2.VideoCapture(0)
#0-default camera(webcam), if you have usb cameras 1,2...etc
#if you need to access a wifi camera, u have to give the ip address
#if you need to access a video file in your computer, give the path to that file
#camera is the video object/source

count=0

while(True):

    ret,img=camera.read()
    # reads a single frame of the video source, ret=0 when the video source is not accesible
    if ret==0:
        print('camera not available')
    else:
        cv2.imshow('LIVE',img)
    cv2.waitKey(1)
    #1 ms delay
