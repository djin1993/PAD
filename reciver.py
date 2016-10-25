import socket, sys
class Receiver:
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8000
    BUFFER = 1024

    connecting_socket = socket.socket()
    connecting_socket.connect((TCP_IP, TCP_PORT))

    letter = connecting_socket.recv(BUFFER)
    #print letter
    while True :
        print letter
        letter = connecting_socket.recv(BUFFER)
    sys.exit()
