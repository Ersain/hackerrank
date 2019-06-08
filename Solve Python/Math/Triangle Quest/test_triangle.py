from TriangleQuest import draw_triangle


def test_triangle_1(capsys):
    draw_triangle(5)
    captured = capsys.readouterr()
    assert captured.out == '1\n22\n333\n4444\n'


def test_triangle_2(capsys):
    draw_triangle(6)
    captured = capsys.readouterr()
    assert captured.out == '1\n22\n333\n4444\n55555\n'


def test_triangle_3(capsys):
    draw_triangle(4)
    captured = capsys.readouterr()
    assert captured.out == '1\n22\n333\n'
