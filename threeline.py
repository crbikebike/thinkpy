__author__ = 'ChrisKristen'

import math

if __name__ == '__main__':

    #functions and stuff
    def newLine():
        print

    def threeLines():
        newLine()
        newLine()
        newLine()

    def nineLines():
        threeLines()
        threeLines()
        threeLines()

    def printTwice(message):
        print message, message

    def concantMachine(firstMessage,secondMessage):
        concantMsg = firstMessage + secondMessage
        printTwice(concantMsg)

      #variables
    bottlecap = 'cats like dogs'

      #actions and stuff
    printTwice("'Spam*4'")

    printTwice(bottlecap)

    math.log10(45)

    concantMachine('hello','kitty')

