from WhatsYourName import print_full_name


def test_print_1():
    assert print_full_name('John', 'Doe') == 'Hello John Doe!\
 You just delved into python.'


def test_print_2():
    assert print_full_name('Alex', 'Hirsch') == 'Hello Alex Hirsch!\
 You just delved into python.'


def test_print_3():
    assert print_full_name('Harry', 'Kane') == 'Hello Harry Kane!\
 You just delved into python.'
