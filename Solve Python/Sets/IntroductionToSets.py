'''
Problem: Introduction to Sets.
Points: 10.

'''


def average(array):
    '''Compute the average of a list with distinct values'''
    return (sum(set(array)))/(len(set(array)))
