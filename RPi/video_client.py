import socket 
import numpy as np
import picamera
from utils import server_address
import time

# Create a TCP/IP socket and establish a connection with server

client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Start connection")

client_sock.connect(server_address)
print("COnnected to the server")

connection = client_sock.makesfile('rb')
