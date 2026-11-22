from greet import farewell, greet, shout, title_case, whisper


def test_greet():
    assert greet("Ada") == "Hello, Ada!"


def test_farewell():
    assert farewell("Ada") == "Goodbye, Ada!"


def test_shout():
    assert shout("hi") == "HI!"


def test_whisper():
    assert whisper("HI") == "hi..."


def test_title_case():
    assert title_case("hello big world") == "Hello Big World"
    assert title_case("ADA lovelace") == "Ada Lovelace"
