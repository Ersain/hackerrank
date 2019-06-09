from TextAlignment import draw_logo


def test_logo_1(capsys):
    draw_logo('H', 1)
    captured = capsys.readouterr()
    captured.out == 'H\nH   H   \nH   H   \nHHHHH \nH   H   \nH   H   \n    H \n'


def test_logo_2(capsys):
    draw_logo('H', 2)
    captured = capsys.readouterr()
    captured.out == ' H \nHHH\n HH      HH     \n HH      HH     \n HH      HH     ' + \
        '\n HHHHHHHHHH \n HH      HH     \n HH      HH     \n HH      HH     \n        HHH \n         H  \n'


def test_logo_3(capsys):
    draw_logo('H', 3)
    captured = capsys.readouterr()
    captured.out == '  H  \n HHH \nHHHHH\n HHH         HHH        ' + \
        '\n HHH         HHH        \n HHH         HHH        \n HHH         HHH        ' + \
        '\n HHHHHHHHHHHHHHH  \n HHHHHHHHHHHHHHH  \n HHH         HHH        ' + \
        '\n HHH         HHH        \n HHH         HHH        \n HHH         HHH        ' + \
        '\n            HHHHH \n             HHH  \n              H   \n'
