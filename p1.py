#!/usr/bin/env python


import socket as skt
import sys

severName = "192.168.1.117"
severPort = 3333

clientSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

clientSocket.connect((severName, severPort))

print "connecting"

while True:

    filename = sys.argv[1]
    f = open(filename, 'rb')
    clientSocket.send(str(filename)+"\r\n\r\n")
    l = f.read(1024)

    while(l):
        num_bytes_sent = clientSocket.send(l)
        while num_bytes_sent <= len(l):
            num = clientSocket.send(l[num_bytes_sent])
        l = f.read
        
    f.close

    print "Done sending"
    print "thank you"
    break
clientSocket.close()
