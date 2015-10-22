#!/usr/bin/env python3

import socket

Host = '127.0.0.1'
Port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, Port))

while 1:
    cmd = b'hdjhdjd'
    s.sendall(cmd)
    data = s.recv(1024)
    print(data)

s.close()
