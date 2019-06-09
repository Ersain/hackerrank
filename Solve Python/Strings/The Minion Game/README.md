# The Minion Game
Kevin and Stuart want to play the 'The Minion Game'.

#### Game Rules
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

#### Scoring
A player gets +1 point for each occurrence of the substring in the string s.

#### For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

#### Input Format
A single line of input containing the string S.
The string S will contain only uppercase letters: [A-Z].

#### Sample Input
```
BANANA
```

#### Sample Output
```
Stuart 12
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
