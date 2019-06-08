# Array Mathematics
You are given two integer arrays, A and B of dimensions NxM. 
Your task is to perform the following operations:

Add ( + )
Subtract ( - )
Multiply ( * )
Integer Division ( / )
Mod ( % )
Power ( ** )


#### Input Format
The first line contains two space separated integers, A and B. 
The next N lines contains M space separated integers of array A. 
The following N lines contains M space separated integers of array B.

#### Sample Input
```python
1 4
1 2 3 4
5 6 7 8
```

#### Sample Output
```python
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 
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
