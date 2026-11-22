from greet import farewell, greet, shout


def test_greet():
    assert greet("Ada") == "Hello, Ada!"


def test_farewell():
    assert farewell("Ada") == "Goodbye, Ada!"


def test_shout():
    assert shout("hi") == "HI!"
