def minion_game(string):
    # your code goes here
    countCons = 0
    countVows = 0
    vowels = 'AEIOU'

    for i in range(len(string)):
        if string[i] in vowels:
            countVows += (len(string)-i)
        else:
            countCons += (len(string)-i)
    if countVows < countCons:
        print('Stuart {}'.format(countCons))
    elif countVows > countCons :
        print('Kevin {}'.format(countVows))
    else:
        print('Draw')

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
