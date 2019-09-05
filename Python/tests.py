#!/usr/bin/env python3

import unittest as ut
from monMath import Matrix

class MatrixTest(ut.TestCase):
    def testInstance(self):
        self.assertIsInstance(Matrix([[1, 2]]), Matrix)
    
    def testIdentity(self):
        self.assertEqual(Matrix.identity(2).getValue(), [[1, 0], [0, 1]])

    def testAdd(self):
        self.assertEqual((Matrix([[1, 2], [3, 4]]) + Matrix([[1, 1],[1, 1]])).getValue(), [[2, 3], [4, 5]])

    def testGetRow(self):
        self.assertEqual(Matrix([[1, 2],[3, 4]]).getRow(1), [3, 4])

    def testGetCol(self):
        self.assertEqual(Matrix([[1, 2], [3, 4]]).getCol(1), [2, 4])
        

if (__name__ == '__main__'):
    ut.main()
