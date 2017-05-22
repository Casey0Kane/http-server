"""This is our server file."""
import socket


def server():
    """Our server function for our sockets."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen(1)
    conn, addr = server.accept()
    message = 'This is our server message.'
    conn.sendall(message.encode('utf8'))
    buffer_length = 8
    message_complete = False
    while not message_complete:
        part = conn.recv(buffer_length)
        print(part.decode('utf8'))
        if len(part) < buffer_length:
            break


if __name__ == '__main__':
    server()
