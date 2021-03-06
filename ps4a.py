# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 12

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    point=0
    for e in word:
        point+=SCRABBLE_LETTER_VALUES.get(e)
    if len(word)==n:
        return 50+point*len(word)
    else:
        return point*len(word)


#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    copia=hand.copy()
    for e in word:
        copia[e]=copia.get(e,0)-1
    return copia



#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    punto=getFrequencyDict(word)
    if word in wordList:
        for e in word:
            if hand.get(e,0)==0:
                return False
            elif punto.get(e,0)>hand.get(e,0):
                return False
    else:
        return False
    return True

def calculateHandlen(hand):
    lista=hand.keys()
    handlen=0
    for e in lista:
        handlen+=hand[e]
    return handlen



def playHand(hand, wordList, n):
    score=0
    keys=hand.keys()
    copia=hand.copy()
    for e in keys:
        copia[e]=0
    z=True
    while z == True: 
        displayHand(hand)
        a=input('Enter word, or a "." to indicate that you are finished:')
        if a == '.':
            return 'Goodbye! Total score:',score
        else:
            if isValidWord(a, hand, wordList)==False:
                print('Invalid word, please try again.')

            else:
                score+=getWordScore(a, n)
                print(a,'earned',getWordScore(a, n),'points. Total score:',score,'points')
                hand=updateHand(hand, a)
                if len(a)==n:
                    z=False
                elif hand==copia:
                    z=False
                    

    return 'Run out of letters. Total score:',score,'points'


#
# Problem #5: Playing a game
# 

def playGame(wordList):
    condition=True
    while condition==True:
        entrada=input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if entrada=='n':
            hand=dealHand(HAND_SIZE)
            copia=hand.copy()
            playHand(copia, wordList, HAND_SIZE)
        elif entrada=='r':
            try:
                playHand(copia, wordList, HAND_SIZE)
            except:
                print('You have not played a hand yet. Please play a new hand first!')
        elif entrada=='e':
            condition=False
        else:
            print('Invalid output')
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
