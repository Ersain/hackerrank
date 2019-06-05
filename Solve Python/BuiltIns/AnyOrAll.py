'''
Problem: Any or All.
Description: Given a list of integers,
If all the integers are positive, 
then check if any integer is a palindromic integer..

'''


N = int(input())
integers = input().split()
print(all(int(i) > 0 for i in integers) and
      any(i == i[::-1] for i in integers))
