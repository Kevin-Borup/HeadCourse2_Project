import socket

ip = '10.108.146.13'
port = 712

keepRunning = True

while keepRunning:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip, port))
    data, address = s.recvfrom(1024)
    sentValue = data.decode('utf-8')
    print("Arduino Sent: ", sentValue, "\n\n")
    if sentValue == 1:
        



# close the socket
s.close()