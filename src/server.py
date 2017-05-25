"""This is our server file."""
import socket
import sys
import os


def server():
    """Our server function for our sockets."""
    server = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen(1)
    while True:
        try:
            conn, addr = server.accept()
            if conn:
                buffer_length = 24
                message_complete = False
                msg = b''
            while not message_complete:
                part = conn.recv(buffer_length)
                msg += part
                if len(part) < buffer_length:
                    break
            if msg[-3:] == 'EOF':
                msg = msg[:-3]
            print(msg.decode('utf8'))
            response = parse_request(msg.decode('utf8'))
            conn.sendall(response.encode('utf8'))
        except KeyboardInterrupt:
            print("\nClosing HTTP server.")
            break
        except(SyntaxError, TypeError):
            response_error()
            print("How did you manage to mess up this badly?")
    conn.close()
    server.close()
    sys.exit()


def response_ok():
    """Send a 200 response."""
    return """HTTP/1.1 200 OK\r\nContent-Type: text/plain \r\n\r\n Successfully connected.\r\n\r\n"""


def response_error(error):
    """Create a 500 server error."""
    err_msg = 'HTTP/1.1 500 Internal Server Error\r\n'
    if len(error) < 3:
        err_msg += 'HTTP Request requires a Method, URI, and a Protocol.\r\n'
    elif len(error) > 3:
        err_msg += 'Unknown arguements passed into request.\r\n'
    else:
        if error[0] != 'GET':
            err_msg += 'This server only accepts GET requests \r\n'
        if error[2] != 'HTTP/1.1':
            err_msg += 'Client must use HTTP/1.1\r\n'
    err_msg += '\r\n'
    return err_msg


def parse_request(header):
    """Parse request from user to see if valid."""
    split_header = header.split()
    if len(split_header) != 3:
        response = response_error(split_header)
    elif split_header[0] != 'GET' or split_header[2] != 'HTTP/1.1':
        response = response_error(split_header)
    else:
        response = response_ok()
    return response


path_file = os.path.abspath('/webroot')


def resolve_uri(path_file):
    """File path to our webroot directory."""
    directory = os.listdir(path_file)
    print('<ul>')
    for item in directory:
        print('<li>%s</li>') % item
        fullpath = os.path.join(path_file, item)
        if os.path.isdir(fullpath):
            resolve_uri(fullpath)
    print('</ul>')
    print(resolve_uri(path_file))


if __name__ == '__main__':
    print("HTTP Server is running.\n")
    server()
