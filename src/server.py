"""This is our server file."""
import socket
import sys
import os
import mimetypes
import io


MEDIA_TYPES = [
    'image/jpg',
    'image/png',
]


def server():
    """Our server function for our sockets."""
    server = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 10000)
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
            header_lines = msg.decode('utf8').split('\r\n')
            split_header = header_lines[0].split()
            if parse_request(split_header):
                response = resolve_uri(split_header[1])
            else:
                response = response_error(split_header)
            conn.sendall(response.encode('utf8'))
        except KeyboardInterrupt:
            print("\nClosing HTTP server.")
            conn.close()
            server.close()
            sys.exit()
            break
        except(SyntaxError, TypeError):
            response_error(split_header)
            print("How did you manage to mess up this badly?")
            conn.close()
            server.close()
            sys.exit()


def response_ok(type, size):
    """Send a 200 response."""
    return "HTTP/1.1 200 OK\r\nContent-Type: " + type + '\r\nContent-Length: ' + size + '\r\n\r\n'


def response_error(error):
    """Create a 500 server error."""
    err_msg = 'HTTP/1.1 500 Internal Server Error\r\n'
    if len(error) < 3:
        err_msg += 'HTTP Request requires 3 items, a Method, URI, and a Protocol.\r\n'
    elif len(error) > 3:
        err_msg += 'Unknown arguements passed into request.\r\n'
    else:
        if error[0] != 'GET':
            err_msg += 'This server only accepts GET requests\r\n'
        if error[2] != 'HTTP/1.1':
            err_msg += 'Client must use HTTP/1.1\r\n'
    err_msg += '\r\n'
    return err_msg


def response_file_not_found(error):
    """Create a 404 error if file is not found in directory.."""
    return 'HTTP/1.1 404 File Not Found\r\n' + error + ' is not in directory.\r\n\r\n'


def parse_request(header):
    """Parse request from user to see if valid."""
    if len(header) != 3:
        return False
    elif header[0] != 'GET' or header[2] != 'HTTP/1.1':
        return False
    return True


def resolve_uri(uri):
    """File path to our webroot directory."""
    root = '../webroot/'
    print("file is", search_directory(root + uri))
    retrieved_file = search_directory(root + uri)
    file_type = mimetypes.guess_type(uri)[0]
    try:
        size = str(os.path.getsize(retrieved_file))
    except IOError:
        size = 0
    print('File Type is: ', file_type)
    try:
        if os.path.exists(retrieved_file):
            if file_type in MEDIA_TYPES:
                f = io.open(retrieved_file, 'rb')
                response = response_ok(file_type, size) + str(f.read())
                f.close()
            elif file_type == 'text/plain':
                response = response_ok(file_type, size)
                f = io.open(retrieved_file)
                response += f.read()
                f.close()
            elif os.path.isdir(root + uri):
                response = response_ok('directory', size) + \
                    prepare_directory(root + uri)
            elif file_type == 'text/html':
                f = io.open(retrieved_file)
                response = response_ok(file_type, size) + str(f.read())
                f.close()
            else:
                f = io.open(retrieved_file)
                response = response_ok(file_type, size) + str(f.read())
                f.close()
        else:
            response = response_file_not_found(uri)
    except IOError():
        return response_file_not_found(uri)
    return response


def prepare_directory(directory):
    """Create html for files in directory."""
    listing = os.listdir(directory)
    response = '<!DOCTYPE html><html><head><title>' + \
        directory + '</title></head><body><ul>'
    for file in listing:
        response += '<li>' + file + '</li>'
    response += '</ul></body></html>'
    return response


def search_directory(uri):
    """Search for files in webroot directory."""
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), uri)


if __name__ == '__main__':
    print("HTTP Server is running.\n")
    server()
