# Merge the Tools

Consider the following:

* A string, s, of length n.
* An integer, k, where k is a factor of n.
We can split s into n/k subsegments where each subsegment, t, consists of a contiguous block of k characters in s. Then, use each t to create string u such that:

* The characters in u are a subsequence of the characters in t.
* Any repeat occurrence of a character is removed from the string such that each character in u occurs exactly once. In other words, if the character at some index j in t occurs at a previous index < j in t, then do not include the character in string u.
Given s and k, print n/k lines where each line i denotes string u.


#### Input Format
The first line contains a single string denoting s. 
The second line contains an integer, k, denoting the length of each subsegment.

#### Sample Input
```
AABCAAADA
3   
```

#### Sample Output
```
AB
CA
AD
```

#### Using with python
```bash
$ python <name>.py
```

#### Using with pyTest
```bash
$ pytest --capture=sys test_<name>.py
or
$ pytest --capture=sys test_<name>.py -v
```
