# Mutations

We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.

Read a given string, change the character at a given index and then print the modified string.

#### Input Format
The first line contains a string, S. 
The next line contains an integer i, denoting the index location and a character c separated by a space.

#### Sample Input
```python
abracadabra
5 k
```

#### Sample Output
```python
abrackdabra
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
