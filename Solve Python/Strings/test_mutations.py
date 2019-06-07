from Mutations import mutate_string


def test_mutate_1():
    assert mutate_string('London', 3, ', ') == 'Lon, don'

def test_mutate_2():
    assert mutate_string('123123123123', 6, ' ') == '123123 123123'

def test_mutate_3():
    assert mutate_string('!@#$%^', 5, '/') == '!@#$%/^'