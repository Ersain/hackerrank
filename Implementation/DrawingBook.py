from math import floor, ceil
#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    if n - p < p:
        if n%2==1:
            return floor((n-p)/2)
        else:
            return ceil((n-p)/2)
    else:
        return floor(p/2)
