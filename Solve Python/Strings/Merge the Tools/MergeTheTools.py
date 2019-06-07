'''
Problem: Merge the Tools!.
Description: Given a string S and integer K,
print len(S)/K strings without
any subsequent occurrences.
E.g.
AABCAAADA, 3 ->
AB, CA, AD

.
Points: 40.

'''


def merge_the_tools(string, k):
    temp = []
    counter = 0
    for i in range(len(string)):
        counter += 1
        if string[i] not in temp:
            temp.append(string[i])
        if counter == k:
            print(''.join(temp))
            temp = []
            counter = 0

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
