from SetAdd import help_rupal


def test_help_rupal_1():
    temp = set()
    help_rupal(temp, 'UK')
    print(temp)
    assert 'UK' in temp


def test_help_rupal_2():
    temp = set()
    help_rupal(temp, 'US')
    help_rupal(temp, 'Russia')
    help_rupal(temp, 'China')
    print(temp)
    assert temp == {'China', 'US', 'Russia'}
