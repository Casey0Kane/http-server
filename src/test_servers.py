"""Testing our functions."""
import pytest

HTTP_TABLE = [
    ['GET /path/to/index.html HTTP/1.1',
        "HTTP/1.1 200 OK\r\nContent-Type: text/plain \r\n\r\Successfully connected."],
    ['GET /to/index.html HTTP/1.1',
        "HTTP/1.1 200 OK\r\nContent-Type: text/plain \r\n\r\nSuccesfully connected."],
    ['GET index.html HTTP/1.1',
        "HTTP/1.1 200 OK\r\nContent-Type: text/plain \r\n\r\nSuccesfully connected."],
    # fails because of PUT instead of GET
    ['PUT /path/to/index.html HTTP/1.1',
        'HTTP/1.1 500 Internal Server Error\r\nThis server only accepts GET requests\r\n\r\n'],
    # fails because HTTP is wrong version
    ['GET /path/to/index.html HTTP/1.0',
        'HTTP/1.1 500 Internal Server Error\r\nClient must use HTTP/1.1\r\n\r\n'],
    # too many arguements
    ['GET /path/to/index.html',
        "HTTP/1.1 500 Internal Server Error\r\nHTTP Request requires a Method, URI, and a Protocol.\r\n\r\n"],
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
        "åΩå∆˚fail") == '''HTTP/1.1 500 Internal Server Error\r\nUnknown arguements passed into request.\r\n\r\n'''


# @pytest.fixture
# def new_parse_request(request):
#     """Make new parse request."""
#     from server import parse_request
#     return parse_request(request)


# def test_parse_request(new_parse_request):
#     """Test requests for either  response ok or response error."""
#     assert hasattr(object, new_parse_request) == header
