# Concatenate
You are given two integer arrays of size NxP and MxP (N & M  are rows, and P is the column).
Your task is to concatenate the arrays along axis 0.


#### Input Format
The first line contains space separated integers N, M and P. 
The next N lines contains the space separated elements of the P columns. 
After that, the next M lines contains the space separated elements of the P columns.

#### Sample Input
```python
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
```

#### Sample Output
```python
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
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
