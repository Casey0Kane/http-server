"""This is our server file."""
import socket
import sys


def server():
    """Our server function for our sockets."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
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

            conn.sendall(msg)
            conn.close()

        except KeyboardInterrupt:
            server.close()
            print("Shutting down echo server. Bye, bye!")
            sys.exit()


if __name__ == '__main__':
    print("Echo server is running\n")
    server()
