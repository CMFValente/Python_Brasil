import statistics

def medNumber ():

    number1 = input ('Enter your first note:')
    number2 = input ('Enter your second note:')
    number3 = input ('Enter yor third note:')
    number4 = input ('Enter your fourth note:')

    listnumber = [float (number1), float (number2), float (number3), float (number4)]

    media = statistics.mean (listnumber)
    print (media)

medNumber ()