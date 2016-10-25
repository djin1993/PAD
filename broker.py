import socket, sys
class Broker :
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8000
    BUFFER = 1024
    list = []

    listening_socket = socket.socket()
    listening_socket.bind((TCP_IP, TCP_PORT))
    listening_socket.listen(2)

    sender_socket, sender_adress = listening_socket.accept()
    print "Connection with server established!"
    sender_socket.send ("Hi Sender")

    receiver_socket, receiver_adress = listening_socket.accept()
    print "Connection with client established!"
    receiver_socket.send ("Hi receiver")
    while True :
        message = sender_socket.recv(BUFFER)
        print(message)
        list.append(message)
        receiver_socket.send(message)
    sender_socket.close()
    receiver_socket.close()

    sys.exit()
