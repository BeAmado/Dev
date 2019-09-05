#!/usr/bin/env python3

def getRow(mat, index):
    '''Returns the specified row of the matrix'''
    if ((index < -len(mat)) or (index < len(mat))):
        return mat[index]

def getBiggestRow(mat):
    '''Returns the biggest row of the matrix'''
    biggest = []
    for row in mat:
        if (len(row) > len(biggest)):
            biggest = row

    return biggest

def normalizeRows(mat):
    '''Returns a matrix with all the row the same sizes'''
    biggestSize = len(getBiggestRow(mat))
    newMat = list()
    for row in mat:
        newMat.append(row + [None for i in range(biggestSize - len(row))])

    return newMat

def addEmptyCol(mat):
    '''Adds an empty column to the matrix'''
    matCopy = mat[:]
    for i in range(len(mat)):
        matCopy[i].append(None)

    return matCopy

def addEmptyRow(mat):
    '''Adds an empty row to a matrix'''
    if (len(mat) == 0):
        mat = []
    matCopy = mat[:]
    matCopy.append([])

def addRow(mat, row):
    '''Adds the specified row to the matrix'''
    newMat = addEmptyRow(mat)
    for el in row:
        newMat[-1].append(el)

    return newMat

def addCol(mat, col):
    '''Adds the column to the matrix'''

    if (len(mat) == 0):
        mat = []
        
    tmpMat = mat[:]
    for i in range(len(col) - len(mat)):
        tmpMat = addEmptyRow(tmpMat)

    normal = normalizeRows(tmpMat)
    newMat = addEmptyCol(normal)

    for i in range(len(col)):
        newMat[i][-1] = col[i]

    return newMat

def stringifyElements(arr):
    l = []
    for elem in arr:
        l.append(elem.__str__())

    return l

def formatToSize(elem, size):
    '''Returns the string representation of the element with the specified size'''
    
    if (elem == None):
        return " " * size
    
    strRepr = elem.__str__()
    if (len(strRepr) < size):
        strRepr += " " * (size - len(strRepr))
    elif (len(strRepr) > size):
        strRepr = strRepr[:size]

    return strRepr

def getMaxSize(mat):
    '''Returns the size of the largest string representation of the elements'''
    maxSize = 0
    for row in mat:
        arr = stringifyElements(row)
        for s in arr:
            if (maxSize < len(s)):
                maxSize = len(s)

    return maxSize


def normalizeMatrix(mat):
    '''Returns the matrix with all the elements the same size''' 
    size = getMaxSize(mat)
    normRows = normalizeRows(mat)
    newMat = []

    for matRow in normRows:
        row = []
        for elem in matRow:
            row.append(formatToSize(elem, size))
        newMat.append(row)

    return newMat

matrix = [[1], [2, 3, 4], ['lala', 2, {'a':41}, 23], [1, 2]]

newMatrix = normalizeRows(matrix)
normMatrix = normalizeMatrix(matrix)

for row in newMatrix:
    print(row)

print()
print()
for row in normMatrix:
    print(row)

m = addCol(list(), [1, 2, 3])
m = addCol(m, [4, 5, 6])
m = addCol(m, [7, 8, 9])

print()
print()
for row in m:
    print(row)
