#!/usr/bin/env python

import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 58430            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Para sair use CTRL+X\n'


def ReceiveLine(socket):
    buff = ""
    c = tcp.recv(1)
    buff += c
    while c != "\x00":
        c = tcp.recv(1)
        buff += c
    return buff

msg = raw_input()
while msg <> '\x18':
    tcp.send (msg + "\x00")
    result = ReceiveLine(tcp)
    print "Received: %s" % result
    msg = raw_input()
tcp.close()
