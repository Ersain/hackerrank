# Complete the countingValleys function below.
def countingValleys(s):
    valleys = 0
    level = 0
    for i in s:
        if i == 'D':
            level -= 1
        else:
            level += 1
        if level == 0 and i == 'U':
            valleys += 1
    return valleys


##s = 'UDDDUDUU'
##print(countingValleys(s))
