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

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
