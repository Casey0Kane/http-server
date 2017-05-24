"""This is our client server."""
import socket


def client(message):
    """Our client function for our sockets."""
    infos = socket.getaddrinfo('127.0.0.1', 5001)
    stream_infos = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_infos[:3])
    client.connect(stream_infos[-1])
    client.sendall(message.encode('utf8'))
    buffer_length = 8
    reply_complete = False
    msg = b' '
    while not reply_complete:
        part = client.recv(buffer_length)
        msg += part
        if len(part) < buffer_length:
            print(msg.decode('utf8'))
            break


if __name__ == '__main__':
    """Our name main."""
    import sys
    message = sys.argv[1]
    client(message)
