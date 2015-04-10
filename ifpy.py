# Determine butt size and number of pies

#just gonna leave this here

def buttFunction(buttNum, pies):
    #butt measurements
    if buttNum <= 6:
        print 'your butt is too small'
    elif buttNum <= 10:
        print 'your butt is like goldilocks'
    else:
        print 'your butt is too big'
    #as long as there is a pie it will get a 'nom'
    while pies > 0:
        print 'nom'
        pies -= 1
    print 'the pie is gone'

#Ask the person running to enter butt size and number of pies
buttFunction(input("how big is your butt?\n"), input("how many pies?\n"))
