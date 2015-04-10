# Determine oat temp and number of pies

#just gonna leave this here

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

#Ask the person running to enter butt size and number of pies
foodFunction(input("how hot is your oatmeal?\n"), input("how many pies?\n"))
