import socket
from tkinter import Image
import CameraControl
import ImageManipulation

ip = '10.108.146.13'
port = 712

keepRunning = True
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while keepRunning:
    s.bind((ip, port))
    data, address = s.recvfrom(1024)
    sentValue = data.decode('utf-8')
    print("Arduino Sent: ", sentValue)
    if sentValue == 1:
        CameraControl.TakePicture()
        ImageManipulation.StartImageProcess()
# close the socket
s.close()