import socket
from tkinter import Image
# import CameraControl
# import ImageManipulation

ip = '10.108.146.13'
port = 712

keepRunning = True
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ip, port))

print("Waiting for arduino")
while keepRunning:
    data, address = s.recvfrom(1024)
    sentValue = data.decode('utf-8')
    print("Arduino Sent: ", sentValue)
    if sentValue == 1:
        # CameraControl.TakePicture()
        # licensePlateExists = ImageManipulation.StartImageProcess()
        licensePlateExists = True
        if licensePlateExists:
            print("Sending Open")
            s.send("Open".encode('utf-8'))
        else:
            print("Sending Close")
            s.send("Close".encode('utf-8'))

        
    

# close the socket
s.close()