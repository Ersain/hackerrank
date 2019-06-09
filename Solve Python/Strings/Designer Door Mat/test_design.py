from DesignerDoorMat import draw_design


def test_draw_1(capsys):
    draw_design(3, 9)
    captured = capsys.readouterr()
    assert captured.out == '---.|.---\n-WELCOME-\n---.|.---\n'


def test_draw_2(capsys):
    draw_design(5, 11)
    captured = capsys.readouterr()
    assert captured.out == '----.|.----\n-.|..|..|.-\n--WELCOME--\n-.|..|..|.-\n----.|.----\n'


def test_draw_3(capsys):
    draw_design(7, 15)
    captured = capsys.readouterr()
    assert captured.out == '------.|.------\n---.|..|..|.---\n.|..|..|..|..|.\n----WEL' + \
        'COME----\n.|..|..|..|..|.\n---.|..|..|.---\n------.|.------\n'
