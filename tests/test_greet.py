from greet import farewell, greet, shout, whisper


def test_greet():
    assert greet("Ada") == "Hello, Ada!"


def test_farewell():
    assert farewell("Ada") == "Goodbye, Ada!"


def test_shout():
    assert shout("hi") == "HI!"


def test_whisper():
    assert whisper("HI") == "hi..."
