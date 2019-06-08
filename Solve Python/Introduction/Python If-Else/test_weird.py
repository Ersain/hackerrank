from PythonIfElse import is_weird


def test_weird_1():
    assert is_weird(3) == "Weird"


def test_weird_2():
    assert is_weird(24) == "Not Weird"


def test_weird_3():
    assert is_weird(14) == "Weird"
