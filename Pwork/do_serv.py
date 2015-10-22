#!/usr/bin/env python3

import socket


Host = '127.0.0.1'
Port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host, Port))
s.listen(1)

while 1:
    # receive the TCP connection, return new socket and ip addr
    conn, addr = s.accept()
    print('connected by :', addr)
    while 1:
        data = conn.recv(1024)  # instance of the data received
        if data == 'exit':
            conn.sendall('Done')
        else:
            conn.sendall('Hello! I receive these data from u:', data)

conn.close()
