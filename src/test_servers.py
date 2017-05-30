"""Testing our functions."""


def test_response_ok():
    """Test that response_ok returns confirmation if connection is valid."""
    from server import response_ok
    assert response_ok() == """
    HTTP/1.1 200 OK\r\n
    Content-Type: text/plain \r\n
    \r\n
    Successfully connected."""


def test_server_error():
    """Test server error function returns connection is unsuccessful."""
    from server import response_error
    assert response_error() == """
    HTTP/1.1 500 Internal Server Error\r\n
    Content-Type: text/plain\r\n
    \r\n
    Could not Successfully connect."""
