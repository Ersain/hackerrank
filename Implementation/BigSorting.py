# Complete the bigSorting function below.
def bigSorting(arr):
    temp = []
    for i in sorted(sorted(arr), key=len):
        temp.append(i)
    return temp
