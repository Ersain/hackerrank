'''
Problem: Collections.OrderedDict().
Description: Given a sequence of sold items,
calculate their total sums and
print the name and total profit of each item.

'''

from collections import OrderedDict

n = int(input())
ord_dict = OrderedDict()

for i in range(n):
    item = input().split()
    item_name = ' '.join(item[:-1])
    if item_name not in ord_dict:
        ord_dict[item_name] = int(item[-1])
    else:
        ord_dict[item_name] += int(item[-1])

for i in ord_dict:
    print(i, ord_dict[i])
