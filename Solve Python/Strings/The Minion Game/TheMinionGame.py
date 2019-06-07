'''
Problem: The Minion Game.
Description: Determine the winner of the game.
Points: 40.

'''


def minion_game(string):
    '''
    Count all the possible words starting
    with either vowels or consonants
    and compare them.
    '''
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
    elif countVows > countCons:
        print('Kevin {}'.format(countVows))
    else:
        print('Draw')
