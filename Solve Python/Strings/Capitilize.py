'''
Problem: Capitalize..
Points: 20.

'''


def capitilize_words(s):
    '''
    Return a capitilized version of a string,
    e.g.
    hello world => Hello World.
    '''
    for i in s.split():
        s = s.replace(i[0], i[0].upper())
    return s
