# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
set_m = set(map(int, input().split()))
n = int(input())
set_n = set(map(int, input().split()))

for i in sorted(list((set_m.union(set_n)).difference(set_m.intersection(set_n)))):
    print(i)
