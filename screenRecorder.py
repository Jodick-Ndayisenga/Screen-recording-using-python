from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
#The module above helps us get the full resolution of the screen
webcam = cv2.VideoCapture(0)

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
name = input("What is your file name?: ").rstrip()
fourcc = cv2.VideoWriter_fourcc("m","p","4","v")
file_name= name+".mp4"
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0,(width, height))

while True:
    im_grab= ImageGrab.grab(bbox=(0,0, width, height))
    im_np = np.array(im_grab)
    #The line below is to transform into original color
    image_final = cv2.cvtColor(im_np, cv2.COLOR_BGR2RGB)
    _, frame = webcam.read()
    fr_height,fr_width,_ = frame.shape
    image_final[0:fr_height, 0:fr_width,:] = frame[0:fr_height, 0:fr_width,:]
    cv2.imshow("Screen capture",image_final)
    captured_video.write(image_final)

    if cv2.waitKey(10) == ord("q"):
        break