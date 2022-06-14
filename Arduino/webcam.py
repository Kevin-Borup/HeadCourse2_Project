# program to capture single image from webcam in python
  
# importing OpenCV library
import cv2 as cv


def TakePicture():
    cam_port = 0
    cam = cv.VideoCapture(cam_port)

    answer, image = cam.read()

    if answer:
        cv.imwrite("LatestLicensePlate.png", image)
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

