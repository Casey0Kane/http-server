"""The file for our gevent concurreny."""


def server(socket, address):
    """Our server using gevent."""
    buffsize = 24
    while True:
        data = socket.recv(buffsize)
        if data:
            socket.sendall(data)
        else:
            socket.close()
            break


if __name__ == '__main__':
    from gevent.server import StreamServer
    from gevent.monkey import patch_all
    patch_all()
    server = StreamServer(('127.0.0.1', 10000), server)
    print('Starting HTTP server on port 10000')
    server.serve_forever()
