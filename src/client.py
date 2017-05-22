"""This is our client server."""
import socket 
import sys


def client(message):
    """open socket connection to server.
send message passed as arg to the server, passed thru socket
accumulate reply sent by server into string and when full reply recieved
close socket and return message
"""
    infos = socket.getaddrinfo('127.0.0.1', 5000)
    stream_infos = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_infos[:3])
    client.connect(stream_infos[-1])
    message = 'This is our client message.'
    client.sendall(message.encode('utf8'))
    buffer_length = 8
    reply_complete = False
    while not reply_complete:
        part = client.recv(buffer_length)
        print(part.decode('utf8'))
        if len(part) < buffer_length:
            break


if __name__ == '__main__':
    client(sys.argv[0])
