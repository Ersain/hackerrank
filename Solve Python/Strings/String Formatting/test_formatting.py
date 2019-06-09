from StringFormatting import print_formatted


def test_format_1(capsys):
    print_formatted(1)
    captured = capsys.readouterr()
    assert captured.out == '1 1 1 1\n'


def test_format_2(capsys):
    print_formatted(2)
    captured = capsys.readouterr()
    assert captured.out == ' 1  1  1  1\n 2  2  2 10\n'


def test_format_3(capsys):
    print_formatted(3)
    captured = capsys.readouterr()
    assert captured.out == ' 1  1  1  1\n 2  2  2 10\n 3  3  3 11\n'
