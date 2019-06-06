'''
Problem: "Find a string".
Points: 10.

'''


def count_substring(string, sub_string):
    '''Count the number of occurences of a substring within a string'''
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()

#     count = count_substring(string, sub_string)
#     print(count)


def test_count():
    assert count_substring('ABCDCDC', 'CDC') == 2
    assert count_substring('HAHAHA', 'AHA') == 2


def test_count_2():
    assert count_substring('ROFL', 'LMAO') == 0
    assert count_substring('AAAA', 'AA') == 3


def test_count_3():
    assert count_substring('PainGain', 'ain') == 2
    assert count_substring('test', 't') == 2
