'''
Problem: "sWAP cASE".
Points: 10.

'''


def swap_case(s):
    '''
    Convert lowercase letters to uppercase
    And vice-versa
    '''
    temp = ''
    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 90:
            temp += chr(ord(s[i]) + 32)
        elif 97 <= ord(s[i]) <= 122:
            temp += chr(ord(s[i]) - 32)
        else:
            temp += s[i]
    return temp

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


def test_swap_1():
    assert swap_case('Swap Case') == 'sWAP cASE'

def test_swap_2():
    assert swap_case('AhAhA') == 'aHaHa'

def test_swap_3():
    assert swap_case('FooBar') == 'fOObAR'
