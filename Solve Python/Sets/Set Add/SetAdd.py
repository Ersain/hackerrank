'''
Problem: Set .add().
Description: Usage of set.add() method.
Points: 10.

'''


def help_rupal(set_a, country):
    set_a.add(country)
    return set_a


if __name__ == "__main__":
    n = int(input())
    countries = set()
    for i in range(n):
        help_rupal(set_a=countries, country=input())
    print(len(countries))
