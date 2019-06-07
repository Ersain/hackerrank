from SetDiscardRemovePop import perform_command


def test_dis_rm_pop_1():
    temp = {1, 2, 3, 4}
    perform_command(temp, 'pop')
    assert temp == set([2, 3, 4])


def test_dis_rm_pop_2():
    temp = {1, 2, 3, 4}
    perform_command(temp, 'remove 2')
    assert temp == set([1, 3, 4])


def test_dis_rm_pop_3():
    temp = {1, 2, 3, 4}
    perform_command(temp, 'discard 1')
    assert temp == set([2, 3, 4])
