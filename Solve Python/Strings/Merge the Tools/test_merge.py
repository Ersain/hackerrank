from MergeTheTools import merge_the_tools


def test_merge_1(capsys):
    merge_the_tools('AABCAAADA', 3)
    captured = capsys.readouterr()
    assert captured.out == 'AB\nCA\nAD\n'


def test_merge_2(capsys):
    merge_the_tools('A', 1)
    captured = capsys.readouterr()
    assert captured.out == 'A\n'


def test_merge_3(capsys):
    merge_the_tools('AADPPRHHY', 3)
    captured = capsys.readouterr()
    assert captured.out == 'AD\nPR\nHY\n'
