from TriangleQuest2 import draw_triangle


def test_triangle_1(capsys):
    draw_triangle(6)
    captured = capsys.readouterr()
    assert captured.out == '1\n121\n12321\n1234321\n123454321\n12345654321\n'


def test_triangle_2(capsys):
    draw_triangle(5)
    captured = capsys.readouterr()
    assert captured.out == '1\n121\n12321\n1234321\n123454321\n'


def test_triangle_3(capsys):
    draw_triangle(4)
    captured = capsys.readouterr()
    assert captured.out == '1\n121\n12321\n1234321\n'
