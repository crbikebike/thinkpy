#This module holds functions that have been written for use when completing the
#open courseware of intro to programming from MIT: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/readings/

# Determine oat temp and number of pies
def foodFunction(oatsTemp, pies):
     #oats temp
        if oatsTemp <= 6:
            print 'your oats are too cold'
        elif oatsTemp <= 10:
            print 'goldilocks just ate all your oats'
        else:
            print 'your oats are hotter than the sun'
        #as long as there is a pie it will get a 'nom'
        while pies > 0:
            print 'nom' + ' I have eaten ' + str(pies) + ' pies'
            pies -= 1
        print 'the pie is gone'

# Tells you the id value the argument holds in computer's memory
def catOrDog(animal):
    memorySpace = id(animal)
    print 'this will always say dog and fyi your argument id is ' + str(memorySpace)

#Demonstrates when a loop is exited because a return value is true, or false if not found
def allTheSums(x, list):

