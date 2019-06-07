'''
Problem: Finding the Percentage.
Description: Given records of N students
with name and grades of 3 subjects.
Then you are given a name,
print the average grade of the student.
E.g.
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Output: 56.00.

Points: 10.


'''

if __name__ == '__main__':
    n = int(input())
    marks = {}
    for i in range(n):
        info = input().split()
        name = info[0]
        scores = list(map(float, info[1:]))
        marks[name] = scores
    target = input()

    res = sum(marks[target])/len(marks[target])

    print("{0:.2f}".format(res))
