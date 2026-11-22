from greet import greet, shout


def test_greet():
    assert greet("Ada") == "Hello, Ada!"


def test_shout():
    assert shout("hi") == "HI!"
