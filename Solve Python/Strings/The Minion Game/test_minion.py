from TheMinionGame import minion_game


def test_minion_1(capsys):
    minion_game('BANANA')
    captured = capsys.readouterr()
    assert captured.out == 'Stuart 12\n'


def test_minion_2(capsys):
    minion_game('BAANANAS')
    captured = capsys.readouterr()
    assert captured.out == 'Kevin 19\n'


def test_minion_3(capsys):
    minion_game('ANANAS')
    captured = capsys.readouterr()
    assert captured.out == 'Kevin 12\n'
