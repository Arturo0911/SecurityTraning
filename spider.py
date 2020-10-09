import socket
import threading
import os
import sys




"""
target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect((target_host, target_port))

client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)

print response
"""

# First, create socket client 


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print("[*] Starting up on {} port {}".format(*server_address))

sock.bind(server_address)

sock.listen(1)

while True:

    print("Esperando por la conexion")
    connection, client_address = sock.accept()

    try:
        print("Conexiondesde: ", client_address)
        
        while True:









