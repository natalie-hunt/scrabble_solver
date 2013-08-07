#!/usr/bin/env python
#
# scrabble.py
#
# A scrabble solver that outputs all valid scrabble words
# given a rack, ordered by score

import sys

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10,"p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

allWords = []
rack     = []

def loadWords():
    dictionary = open('sowpods.txt', 'r')
    for line in dictionary:
        allWords.append(line.strip('\r\n').lower())
    dictionary.close()
    return allWords

def getRack():
    try:
        return list(sys.argv[1].lower())
    except:
        print "You must supply a rack of letters"
        print "i.e. $ python scrabble.py ABCDEFG"
        sys.exit()

def checkWord(word, rack):
    _rack = list(rack) # preserve the rack list
    for letter in word:
        if letter in _rack:
            _rack.remove(letter)
        else:
            return False
    return True

def findValidWords(rack):
    validWords = []
    for word in allWords:
        if checkWord(word, rack):
            validWords.append(word)
    return validWords

def scoreWord(word):
    score = 0
    for letter in word:
        score += int(scores[letter])
    return score

def scoreAllWords(words):
    scoredWords = {}
    for word in words:
        scoredWords[word] = scoreWord(word)
    return scoredWords

def sort(dictionary):
    # returns a sorted tuple, not a dict (dicts are not sortable)
    return sorted(dictionary.items(), key = lambda x: x[1], reverse=True)

def output(scoredWords):
    for word, score in scoredWords:
        print score, word

def main():
    rack = getRack()
    loadWords()
    validWords = findValidWords(rack)
    scoredWords = scoreAllWords(validWords)
    scoredWords = sort(scoredWords)
    output(scoredWords)

if __name__ == '__main__': main()
