from http import server
import socket
import sys

ip = '10.108.149.20'
port = 712

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    send_data = input("Type some text to send =>")
    s.sendto(send_data.encode('utf-8'), (ip, port))
    print("\n\n 1. Client Sent : ", send_data, "\n\n")
    data, address = s.recvfrom(712)
    print("\n\n 2. Client received : ", data.decode('utf-8'), "\n\n")
# close the socket
s.close()