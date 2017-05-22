"""This is our server file."""
import socket


def server():
    """ When ran it should start a server.
    continue running/send response for msg recieved
    keyboard interupt (ctrl +c) cleanly exit  ( all sockets closed )
    accept incoming connections/ messages sent from them and echo them back as received
    msg recieved & echoes the conn. shoul be close - but server must remain running and accepting connections
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen(1)
    conn, addr = server.accept()
    buffer_length = 8
    message_complete = False
    while not message_complete:
        part = conn.recv(buffer_length)
        print(part.decode('utf8'))
        if len(part) < buffer_length:
            break
    message = 'This is our server message.'
    conn.sendall(message.encode('utf8'))

if __name__ == '__main__':
    server()