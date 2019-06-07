from SetMutations import perform_command


def test_mutation_1():
    temp1 = {1, 2, 3, 4, }
    temp2 = {2, 4, 1, 6, }
    perform_command(temp1, temp2, 'intersection_update')
    print(temp1)
    assert temp1 == set([1, 2, 4, ])


def test_mutation_2():
    temp1 = {1, 2, 3, 4, }
    temp2 = {2, 4, 1, 6, }
    perform_command(temp1, temp2, 'difference_update')
    print(temp1)
    assert temp1 == {3}


def test_mutation_3():
    temp1 = {1, 2, 3, 4, }
    temp2 = {2, 4, 1, 6, }
    perform_command(temp1, temp2, 'symmetric_difference_update')
    print(temp1)
    assert temp1 == set([3, 6, ])
