# No Idea!

There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. 
For each i integer in the array, if i in A, you add 1 to your happiness. If i in B, you add -1 to your happiness. 
Otherwise, your happiness does not change. Output your final happiness at the end.

#### Input Format
The first line contains integers n and m separated by a space. 
The second line contains n integers, the elements of the array. 
The third and fourth lines contain m integers, A and B, respectively.

#### Sample Input
```python
3 2
1 5 3
3 1
5 7
```

#### Sample Output
```python
1
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
