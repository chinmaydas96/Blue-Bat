import socket
import numpy as np
from util import server_address

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
