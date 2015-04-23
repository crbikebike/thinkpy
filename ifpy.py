# This library holds functions that have been written for use when completing the
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


#Write a procedure that takes a list of numbers, nums, and a limit, limit,
# and returns a list which is the shortest prefix of nums the sum of whose values is
# greater than limit. Use for. Try to avoid using explicit indexing into the list.
def prefixLimit(nums, limit):
    prefix = []
    sum = 0
    for num in nums:
        sum += num
        prefix.append(num)
        if sum > limit:
            return prefix


def rangerDanger(n):
        rangeSum = 0
        numRange = range(n)
        for num in numRange:
            rangeSum += num*num
        return rangeSum

