# Complete the findDigits function below.
def findDigits(n):
    counter = 0
    r = n
    while r > 0:
        if n%10!=0 and (n%(r%10)==0):
            counter += 1
        r = r//10
    return counter

