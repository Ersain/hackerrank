from StringValidators import is_valid


def test_valid_1(capsys):
    is_valid('qA2')
    captured = capsys.readouterr()
    captured.out == 'True\nTrue\nTrue\nTrue\nTrue\n'


def test_valid_2(capsys):
    is_valid('123')
    captured = capsys.readouterr()
    captured.out == 'True\nFalse\nTrue\nFalse\nFalse\n'


def test_valid_3(capsys):
    is_valid('#$%@^&*')
    captured = capsys.readouterr()
    captured.out == 'False\nFalse\nFalse\nFalse\nFalse\n'
