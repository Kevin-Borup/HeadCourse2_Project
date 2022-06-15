# program to capture single image from webcam in python
  
# importing OpenCV library
import cv2 as cv
import pygame
import pygame.camera
import time

def TakePicturePy():
    pygame.init()
    pygame.camera.init()
    camlist =pygame.camera.list_cameras() #Camera detected or not
    cam = pygame.camera.Camera(camlist[1],(3840,2160))
    cam.start()
    time.sleep(1.5)
    img = cam.get_image()
    pygame.image.save(img,"Arduino\Pictures\LatestLicensePlate.png")
    cam.stop()

TakePicturePy()
# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
# cam_port = 0
# cam = cv.VideoCapture(cam_port)
  
# # reading the input using the camera
# answer, image = cam.read()
  
# # If image will detected without any error, 
# # show result
# if answer:
  
#     # showing result, it take frame name and image 
#     # output
#     cv.imshow("LatestLicensePlate", image)
  
#     # saving image in local storage
#     cv.imwrite("LatestLicensePlate.png", image)
  
#     # If keyboard interrupt occurs, destroy image 
#     # window
#     cv.waitKey(0)
#     cv.destroyWindow("LatestLicensePlate")
  
# # If captured image is corrupted, moving to else part
# else:
#     print("No image detected. Please! try again")

