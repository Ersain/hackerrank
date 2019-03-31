n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    temp_list = list(input().split())
    if temp_list[0] == 'pop':
        s.pop()
    elif temp_list[0] == 'remove':
        s.remove(int(temp_list[1]))
    elif temp_list[0] == 'discard':
        s.discard(int(temp_list[1]))

print(sum(s))
