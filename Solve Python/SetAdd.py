# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a_set = set()
for i in range(n):
    a_set.add(input())
print(len(a_set))
