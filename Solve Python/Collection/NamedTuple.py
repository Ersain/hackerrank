'''
Problem: Collections.namedtuple().
Description: Calculate the average marks of the students
according to some column.

'''

n = int(input())
columns = input().split()
marks_col = columns.index("MARKS")

all_marks = [int(input().split()[marks_col]) for i in range(n)]
print(sum(all_marks)/len(all_marks))
