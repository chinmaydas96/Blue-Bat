"""import socket
import numpy as np
from utils import server_address

class VideoStreaming:
    def __init__(self):

        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind(server_address)

        # Listen for incoming connection
        sock.listen(1)
        print("Listening connection")

        # Accept a single connection
        self.connection, self.client_address = self.sock.accept()
        self.connection = self.connection.makefile('rb')
        self.stream_video()

"""
"""capture_video_server_test.py: Server code for capturing video from rpi """

import cv2
import numpy as np
import socket
import struct
from utils import *


class VideoStreamingTest:
    def __init__(self):
        # Create a TCP/IP socket and listen for connections on COMP_IP_ADDRESS:8000
        # Don't forget to allow the port on the windows firewall settings

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(server_address)

        self.server_socket.listen(1)
        print('Listening for connection...')

        # Accept a single connection and make a file like object out of it
        self.connection, self.client_address = self.server_socket.accept()
        self.connection = self.connection.makefile('rb')
        self.stream_video()

    def stream_video(self):
        frame = 0
        # faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        try:
            print('Connection from: {0}'.format(self.client_address))
            print('Streaming...')
            print("Press 'q' to exit")

            while True:
                # Obtain the length of the frame streamed over the connection. If image_len = 0, close the
                # connection
                image_len = struct.unpack('<L', self.connection.read(struct.calcsize('<L')))[0]
                if not image_len:
                    break

                # Store bytes in a string
                recv_bytes = b''
                recv_bytes += self.connection.read(image_len)

                # Read an image from buffer in memory
                image = cv2.imdecode(np.fromstring(recv_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)

                frame += 1

                # Show the frame
                # cv2.imshow('Video', image)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                #faces = faceCascade.detectMultiScale(gray, 1.3, 5)
                #for (x, y, w, h) in faces:
                #	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.imshow('Video', image)









                if (cv2.waitKey(5) & 0xFF) == ord('q'):
                    break

        finally:
            print('Closing the connection.')
            self.connection.close()
            self.server_socket.close()
            print("Number of frames received: {0}".format(frame))


if __name__ == '__main__':
    VideoStreamingTest()        
