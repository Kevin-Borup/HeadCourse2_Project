import pygame
import pygame.camera
import time

def TakePicture():
    pygame.init()
    pygame.camera.init()
    camlist =pygame.camera.list_cameras() #Camera detected or not
    cam = pygame.camera.Camera(camlist[0],(3840,2160))
    cam.start()
    time.sleep(1.5)
    img = cam.get_image()
    pygame.image.save(img,"LatestLicensePlate.png")
    cam.stop()