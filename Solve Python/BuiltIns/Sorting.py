'''
Problem: gnitroS.
Description: Given a string S.
Sort S in this form:
lowerCase > upperCase > (odds > evens).digits.
E.g.
Sorting1234 -> ginortS1324.

'''


a = input()

lowers = sorted([i for i in a if i.islower()])
uppers = sorted([i for i in a if i.isupper()])
evens = sorted([i for i in a if i.isdigit() and int(i) % 2 == 0])
odds = sorted([i for i in a if i.isdigit() and int(i) % 2 == 1])

print(''.join((lowers + uppers + odds + evens)))
