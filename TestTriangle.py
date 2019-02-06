# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testIfValidInput1(self):
        self.assertEqual(classifyTriangle(300, 4, 5), 'InvalidInput')

    def testIfValidInput2(self):
        self.assertEqual(classifyTriangle(3, 400, 5), 'InvalidInput')
    
    def testIfValidInput3(self):
        self.assertEqual(classifyTriangle(3, 4, 500), 'InvalidInput')
    
    def testIfValidInput4(self):
        self.assertEqual(classifyTriangle(-20, 4, 5), 'InvalidInput')
    
    def testIfValidInput5(self):
        self.assertEqual(classifyTriangle(3, -4, 5), 'InvalidInput')
    
    def testIfValidInput6(self):
        self.assertEqual(classifyTriangle(3, 4, -5), 'InvalidInput')

    def testIfValidInput7(self):
        self.assertEqual(classifyTriangle(0, 4, 5), 'InvalidInput')

    def testIfValidInput8(self):
        self.assertEqual(classifyTriangle(0, 4, 'g'), 'InvalidInput')

    def testIfInteger(self):
        self.assertEqual(classifyTriangle(3.5,4,5), 'InvalidInput')

    def testIsTriangle1(self):
        self.assertEqual(classifyTriangle(3,4,9), 'NotATriangle')
    
    def testIsTriangle2(self):
        self.assertEqual(classifyTriangle(5,7,9), 'Scalene')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5), 'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')
    
    def testIsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(4,4,6), 'Isosceles')
    
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(6, 12, 14), 'Scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(verbosity=2, exit=False)

