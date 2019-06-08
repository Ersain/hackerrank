# Check Strict Superset

You are given a set A and n other sets. 
Your job is to find whether set A is a strict superset of each of the n sets.
Print True, if A is a strict superset of each of the n sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset.

#### Sample Input
```python
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
```

#### Sample Output
```python
False
```

#### Using with python
```bash
$ python <name>.py
```

#### Using with pyTest
```bash
$ pytest test_<name>.py
or
$ pytest test_<name>.py -v -s
```
