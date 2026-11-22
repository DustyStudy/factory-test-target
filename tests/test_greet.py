from greet import farewell, greet, reverse_words, shout, whisper


def test_greet():
    assert greet("Ada") == "Hello, Ada!"


def test_farewell():
    assert farewell("Ada") == "Goodbye, Ada!"


def test_shout():
    assert shout("hi") == "HI!"


def test_whisper():
    assert whisper("HI") == "hi..."


def test_reverse_words():
    assert reverse_words("one two three") == "three two one"
    assert reverse_words("solo") == "solo"
