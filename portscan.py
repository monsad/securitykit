import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 443

def portscanner(port):
    if sock.connect_ex((host, port)):
        print("Port %d is closed" % port)
    else:
        print("Port %d is opened" % port)

portscanner(port)

