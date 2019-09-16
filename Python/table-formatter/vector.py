#!/usr/bin/env python3

from matrix import *

def addSpacesBefore(s, amount):
    spaces = ''
    for i in range(amount):
        spaces += ' '
    return spaces + str(s)

def addSpacesAfter(s, amount):
    spaces = ''
    for i in range(amount):
        spaces += ' '
    return str(s) + spaces

def addSpacesAround(s, amountBefore, amountAfter):
    return addSpacesBefore(addSpacesAfter(s, amountAfter), amountBefore)

def processElement(s, args):
    if (s == None):
        s = ''

    if (args['addSpaceAroundElement']):
        return addSpacesAround(s, 1, 1)
    else:
        return s

def processSeparator(s, args):
    if (args['addSpaceAroundSeparator']):
        return addSpacesAround(s, 1, 1)
    else:
        return s

def vectorToString(v, args):
    vecStr = ''

    spaceFormatting = {
        'addSpaceAroundElement': args['addSpaceAroundElement'],
        'addSpaceAroundSeparator': args['addSpaceAroundSeparator']
    }

    # put the character marking beginning
    vecStr += args['beg']

    for i in range(len(v)):
        # adding the element
        vecStr += processElement(v[i], spaceFormatting)

        # adding the separator
        if (i < (len(v) - 1)): # only adds the separator if it is not the last element
            vecStr += processSeparator(args['sep'], spaceFormatting)

    # put the character marking the end
    vecStr += args['end']

    return vecStr

def showVector(v, sep = '|', beg = '[', end = ']', putSpaces = True):
    formatting = {
        'addSpaceAroundElement' : putSpaces,
        'addSpaceAroundSeparator' : False,
        'sep': sep,
        'beg': beg,
        'end': end
    }

    print(vectorToString(v, formatting))

def getBiggestElement(l):
    '''Returns the biggest element of a list'''
    if (len(l) == 0):
        return None

    biggest = ''
    for elem in l:
        if (
            elem != None and 
            len(str(elem)) > len(str(biggest))
        ):
            biggest = elem

    return biggest

def formatStrToSize(s, size, align = 'left'):
    '''Returns a string formatted with spaces'''

    myStr = ''

    if (s != None):
        myStr = str(s)

    if (size < len(myStr)):
        return myStr[:size]

    totalAmountSpaces = size - len(myStr)

    if (align == 'left'):
        myStr = addSpacesAfter(myStr, totalAmountSpaces)

    elif (align == 'right'):
        myStr = addSpacesBefore(myStr, totalAmountSpaces)

    elif (align == 'center'):
        leftSpaces = totalAmountSpaces // 2
        rightSpaces = totalAmountSpaces - leftSpaces
        myStr = addSpacesAround(myStr, leftSpaces, rightSpaces)

    return myStr

def listIsNumeric(l):
    '''Checks if all the elements in the list are numeric'''
    try:
        for elem in l:
            if (elem != None):
                float(elem)
                int(elem)

    except ValueError:
        return False

    return True

def normalizeLengths(l, align = 'left'):
    '''Returns a list with all the elements as strings of the same size.'''
    
    if listIsNumeric(l):
        align = 'right'

    size = len(str(getBiggestElement(l)))
    newList = []

    for elem in l:
        newList.append(formatStrToSize(elem, size, align))

    return newList

def normalizeMatrix(mat):
    matT = transpose(mat)
    newMat = []
    for row in matT:
        newMat.append(normalizeLengths(row))

    return transpose(newMat)

def createRowSeparators(mat, char):
    row = mat[0]
    rowSeparators = []
    for elem in row:
        rowSeparators.append(char * len(str(elem)))

    return rowSeparators
        

def showMatrix(mat):

    newMat = normalizeMatrix(mat)
    rowSeparators = createRowSeparators(newMat, '-')
    asterisks = createRowSeparators(newMat, '*')

    showVector(asterisks, '***', '**', '**', False)
    
    for i in range(len(newMat)):
        showVector(getRow(newMat, i), '|', '|', '|')

        if (i < len(newMat) - 1):
            showVector(rowSeparators, '-+-', '+-', '-+', False)

    showVector(asterisks, '***', '**', '**', False)
    

myMatrix = [
    [1, 'Charmander', 'Bla bla', 23, 'lala'],
    [3, 'Ivete', '21'],
    [234, 121, 2, -89],
    [-890,'Hallowed Be Thy Name', 'Will', 1, 2]
]
print()
showMatrix(myMatrix)
print()
