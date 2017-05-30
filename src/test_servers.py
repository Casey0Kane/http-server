"""Testing our functions."""
import pytest

HTTP_TABLE = [
    ['GET a_web_page.html HTTP/1.1',
        "HTTP/1.1 200 OK\r\nContent-Type: text/plain \r\n\r\n Successfully connected.\r\n\r\n"],
    ['GET make_time.py HTTP/1.1',
        """HTTP/1.1 200 OK\r\nContent-Type: text/plain \r\n\r\n Successfully connected.\r\n\r\n"""],
    ['GET sample.txt HTTP/1.1',
        """HTTP/1.1 200 OK\r\nContent-Type: text/plain \r\n\r\n Successfully connected.\r\n\r\n"""],
    # fails because of PUT instead of GET
    ['PUT /path/to/index.html HTTP/1.1',
        'HTTP/1.1 500 Internal Server Error\r\nThis server only accepts GET requests \r\n\r\n'],
    # fails because HTTP is wrong version
    ['GET /path/to/index.html HTTP/1.0',
        'HTTP/1.1 500 Internal Server Error\r\nClient must use HTTP/1.1\r\n\r\n'],
    # too many arguements
    ['GET /path/to/index.html',
        "HTTP/1.1 500 Internal Server Error\r\nHTTP Request requires 3 items, a Method, URI, and a Protocol.\r\n\r\n"],
    # too many arguements
    ['GET /path/to/index.html HTTP/1.1 Potato',
        "HTTP/1.1 500 Internal Server Error\r\nUnknown arguements passed into request.\r\n\r\n"],
]


@pytest.mark.parametrize("message, response", HTTP_TABLE)
def test_message_buffer(message, response):
    """Test message is variations of the buffer."""
    from client import client
    assert client(message) == response


def test_server_error():
    """Test server error."""
    from server import response_error
    assert response_error(
        "failure") == '''HTTP/1.1 500 Internal Server Error\r\nUnknown arguements passed into request.\r\n\r\n'''
