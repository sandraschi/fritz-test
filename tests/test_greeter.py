"""Tests for fritz_test.greeter."""

from fritz_test.greeter import add, greet


def test_greet():
    assert greet("World") == "Hello, World!"


def test_add():
    assert add(2, 3) == 5
