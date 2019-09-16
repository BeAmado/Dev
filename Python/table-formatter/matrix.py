#!/usr/bin/env python3

def checkAllRowsHaveSameSize(mat):
    '''Returns true if all the rows of the matrix are the same length.
    Otherwise returns false.'''
    size = len(mat[0])
    for row in mat:
        if len(row) != size:
            return False

    return True

def getRow(mat, m):
    '''Returns the m-th row of the matrix'''
    if ((m >= len(mat)) or (m < 0)):
        return None
    return mat[m]

def getCol(mat, n):
    '''Returns the n-th column of the matrix'''
    if (not checkAllRowsHaveSameSize(mat)):
        return None
    elif (n >= len(mat[0]) or n < 0):
        return None

    col = []
    for row in mat:
        col.append(row[n])

    return col

def copyMatrix(mat):
    newMat = []
    for row in mat:
        newRow = []
        for elem in row:
            newRow.append(elem)
        newMat.append(newRow)

    return newMat

def concatColumn(mat, col):
    '''Returns a new matrix with the column concatenated at the end'''
    if ((not checkAllRowsHaveSameSize(mat)) or (len(mat) != len(col))):
        return None

    newMatrix = copyMatrix(mat)

    for i in range(len(col)):
        newMatrix[i].append(col[i])

    return newMatrix

def getBiggestLengthRow(mat):
    '''Returns the row that has the most elements'''
    biggestRow = mat[0][:]
    for row in mat:
        if len(row) > len(biggestRow):
            biggestRow = row[:]

    return biggestRow

def addEmptyElements(vect, amount):
    newVect = vect[:]
    for i in range(amount):
        newVect.append(None)

    return newVect

def fillVectorToSize(vect, size):
    return addEmptyElements(vect, size - len(vect))

def putAllRowsTheSameSize(mat):
    '''Returns a new matrix with all the rows having the same amount of elements.'''
    newMat = []
    length = len(getBiggestLengthRow(mat))

    for row in mat:
        newMat.append(fillVectorToSize(row, length))

    return newMat

def transpose(mat):
    '''Returns the transpose of the matrix.'''

    newMat = mat[:]

    if (not checkAllRowsHaveSameSize(mat)):
        newMat = putAllRowsTheSameSize(mat)

    transposed = []
    for j in range(len(newMat[0])):
        transposed.append(getCol(newMat, j))

    return transposed

