import pytest
from src.string_utils import to_uppercase, to_lowercase, reverse_string

def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
    assert to_uppercase("Hello123") == "HELLO123"
    assert to_uppercase("") == ""  # empty test

def test_to_lowercase():
    assert to_lowercase("HELLO") == "hello"
    assert to_lowercase("Hello123") == "hello123"
    assert to_lowercase("") == ""  # empty test

def test_reverse_string():
    assert reverse_string("abcd") == "dcba"
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""  # empty test