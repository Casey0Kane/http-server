"""This is our client server."""
import socket
import sys


def client(message):
    """Our client function for our sockets."""
    infos = socket.getaddrinfo('127.0.0.1', 5000)
    stream_infos = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_infos[:3])
    client.connect(stream_infos[-1])
    buffer_length = 24
    client.sendall(message.encode('utf8'))
    msg = b''
    reply_complete = False
    while not reply_complete:
        part = client.recv(buffer_length)
        msg += part
        if len(part) < buffer_length:
            break
    client.close()
    print(msg.decode('utf8'))
    return(msg.decode('utf8'))


if __name__ == '__main__':
    """Our name main."""
    client(sys.argv[1])
