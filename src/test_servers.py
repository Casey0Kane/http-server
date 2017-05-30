"""Testing our functions."""
from client import client


def test_message_less_than_buffer():
    """Test message is smaller than the buffer."""
    assert client("message") == "message"


def test_message_larger_than_buffer():
    """Test message is smaller than a buffer."""
    assert client("Message is super long and won't be shorter than 8") == "Message is super long and won't be shorter than 8"


def test_message_same_as_buffer():
    """Test message is same as the buffer."""
    assert client("MsgEIGHT") == "MsgEIGHT"


"""msg cont non-ascii chars:.
    assert msg sent = reply recieved"""
