from HelloWorld import hello_world


def test_hello_1(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == 'Hello, World!\n'


def test_hello_2(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == 'Hello, World!\n'


def test_hello_3(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == 'Hello, World!\n'
