'''
Problem: Introduction to Sets.

'''


def average(array):
    '''Compute the average of a list with distinct values'''
    return (sum(set(array)))/(len(set(array)))
