import socket



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



host = input("This is host: ")
port = input("This is port to scan: ")


def portscanner(port):
    if sock.connect_ex((host,port)):
        print("Port %d is closed" % port)
    else:
        print("Port %d is opened" % port)


portscanner(port)
