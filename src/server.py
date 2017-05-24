"""This is our server file."""
import socket
import sys


CRLF = b" \r\n\r\n"


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


def response_error(self, error_code, reason_phrase):
    """Send a 500 Server Error."""
    error_code = 'HTTP/1.1 500 Internal Server Error<CRLF>'
    reason_phrase = """Content-Type: text/plain<CRLF>
    <CRLF>
    Could not Successfully connect."""
    error_msg = error_code + reason_phrase
    return error_msg


def parse_request(request):
    """Check request and send to either response_ok or response_error."""
    request = 'GET /path/to/index.html HTTP/1.1<CRLF>'
    'Host:  www.example.com:80<CRLF>'
    '<CRLF>'
    if request == response_ok():
        return response_ok()
        print(response_ok)
    else:
        return response_error(request)
        print(response_error)


if __name__ == '__main__':
    print("Echo server is running\n")
    server()
