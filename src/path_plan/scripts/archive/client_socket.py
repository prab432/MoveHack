#! /usr/bin/env python

import socket
import time

def req_top():
	hostname = socket.gethostname()
	port_top = 12345 # front
	client_top = socket.socket()
	client_top.connect((hostname,port_top))
	client_top.send("get")
	temp = client_top.recv(1024)
	client_top.close()
	return temp

def req_front():
	hostname = socket.gethostname()
	port_front = 12346 # front
	client_front = socket.socket()
	client_front.connect((hostname,port_front))
	client_front.send("get")
	temp = str(client_front.recv(1024))
	client_front.close()
	return temp

for i in range(0,100):
	print req_front().split(',')[:]
	print req_top().split(',')[:]
