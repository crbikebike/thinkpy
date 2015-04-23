__author__ = 'ChrisKristen'

#writing along with the book here: http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap07.html

fruit = 'banana'

#7.3 traversal example

def forwardsLetters(text4me):
    index = 0
    while index < len(text4me):
        letter = text4me[index]
        print letter
        index += 1

def backwardsLetters(text4me):
    index = len(text4me) - 1
    while index >= 0:
        letter = text4me[index]
        print letter
        index -= 1

def duckNames(prefix,suffix):
    for letter in prefix:
        if letter == 'O':
            print letter + 'u' + suffix
        elif letter == 'Q':
            print letter + 'u' + suffix
        else:
            print letter + suffix

def eurekaLoop(text,ch,startPoint):
    index = startPoint
    while index < len(text):
        if text[index] == ch:
            return index
        index += 1
    return -1

def traverseCountLetters(text,letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    return count

def findCountLetters(text,letter,startPoint):
    count = 0
    index = startPoint
    while index < len(text):
        if text[index] == letter:
            count += 1
        index += 1
    return count

