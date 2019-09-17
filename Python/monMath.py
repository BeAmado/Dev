#!/usr/bin/env python3

class Matrix(list):
    def __valid(self, mat):
        if (not isinstance(mat, list) or len(mat) == 0):
            return False
        if (not isinstance(mat[0], list) or len(mat[0]) == 0):
            return False
        return True

    def __init__(self, mat):
        if (self.__valid(mat)):
            self.__data = mat[:]
            self.__nrows = len(mat)
            self.__ncols = len(mat[0])
        else:
            self.__data = []
            self.__nrows = 0
            self.__ncols = 0

    def getValue(self):
        return self.__data[:]

    def identity(size):
        return Matrix([
            [1 if j == i else 0 for j in range(size)] for i in range(size)
        ])

    def getDimensions(self):
        """Returns the dimensions in a dictionary with keys 
        'cols' and 'rows'."""
        return {'cols': self.__ncols, 'rows': self.__nrows}

    def isMatrix(mat):
        return isinstance(mat, Matrix)

    def __validMatrix(self, other):
        return isinstance(other, Matrix) and self.__valid(other.getValue())
    
    def __sameDimensions(self, mat):
        if (not self.__validMatrix(mat)):
            return False

        return (
            (self.__ncols == mat.getDimensions()['cols']) and 
            (self.__nrows == mat.getDimensions()['rows'])
        )

    def __add__(self, other):
        if (not self.__sameDimensions(other)):
            return None
        
        return Matrix([
            [
                (
                    self.getValue()[i][j] + other.getValue()[i][j]
                ) for j in range(self.__ncols)
            ] for i in range(self.__nrows)
        ])

    def getRow(self, n):
        """Returns the nth row, 0 <= n"""
        if (n >= 0 and n < self.__nrows):
            return self.getValue()[n]
        
    def getCol(self, n):
        """Returns the nth column, 0 <= n"""
        if (n >= 0 and n < self.__ncols):
            return [self.getValue()[i][n] for i in range(self.__nrows)]


