"""This is our server file."""
import socket
import sys


def server():
    """Our server function for our sockets."""
    server = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5001)
    server.bind(address)
    server.listen(1)
    while True:
        try:
            conn, addr = server.accept()
            buffer_length = 8
            message_complete = False
            msg = b' '
            while not message_complete:
                part = conn.recv(buffer_length)
                msg += part
                if len(part) < buffer_length:
                    break
            conn.sendall(response_ok().encode('utf8'))
            print('Connection succesfull!')
            conn.close()
        except KeyboardInterrupt:
            print("\nClosing echo server.")
            break
        except(RuntimeError, SyntaxError, UnicodeError):
            conn.sendall(response_error().encode('utf8'))
            print("How did you manage to mess up this badly?")
    server.close()
    sys.exit()


def response_ok():
    """Send a 200 response."""
    return """
    HTTP/1.1 200 OK\r\n
    Content-Type: text/plain \r\n
    \r\n
    Successfully connected."""


def response_error():
    """Send a 500 Server Error."""
    return """
    HTTP/1.1 500 Internal Server Error\r\n
    Content-Type: text/plain\r\n
    \r\n
    Could not Successfully connect."""


def parse_request():
    """Check request and send to either response_ok or response_error."""
    pass


if __name__ == '__main__':
    print("Echo server is running\n")
    server()
