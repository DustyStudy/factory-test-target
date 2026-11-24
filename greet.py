"""Small helpers used to test the issue factory."""


def greet(name: str) -> str:
    return f"Hello, {name}!"


def farewell(name: str) -> str:
    return f"Goodbye, {name}!"


def shout(text: str) -> str:
    return f"{text.upper()}!"


def whisper(text: str) -> str:
    return f"{text.lower()}..."


def reverse_words(text: str) -> str:
    return " ".join(reversed(text.split()))


def repeat_text(text: str, times: int) -> str:
    if times < 0:
        raise ValueError("times must be zero or more")
    return text * times
