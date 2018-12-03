#This file runs the tests and launch the main menu function of the calculator (user interface)
#tests successful: 'ran 10 tests in 0.031s'

import unittest #import unittest library (file unittest.py)

#import all the function from the calc file:
from calc_list import add, multiply, substract, divide, exponent, square, squareRoot, cube, factorial, cosinus, MainMenu

#define class to run  tests for each calculation function:
class calculatorTest (unittest.TestCase):
        def testAdd (self):
            self.assertEqual (7, add ([2, 2, 3]))
            self.assertEqual (-4, add ([2,-2,-4])) #test addition including negative numbers
            
        def testMultiply (self):
            self.assertEqual (12, multiply ([2, 2, 3]))
            self.assertEqual (16, multiply ([2,-2,-4]))#test mutiplication including  negative numbers         
          
        def testSubstract (self):
            self.assertEqual ([1, 1, 1], substract ([2, 2, 2], [1, 1, 1]))
            self.assertEqual ([1, 5], substract ([2, 4], [1, -1, 1])) #test with negative numbers in the list and different list size
            self.assertEqual ([4, 3, 2], substract ([1, 4, 3, 2], [-3, 1, 1])) # test with negative numbers in the result and different list size
            
        def testDivide (self):
            self.assertEqual ([2, 0.2, 1], divide ([2, 2, 1], [1, 10, 1]))
            self.assertEqual ([2, -2, -2], divide ([2, 4, -6], [1, -2, 3, 4]))#test negative numbers and different list sizes
            self.assertEqual ([1, 'division by 0 not allowed', 0.25], divide ([2, 3, 1], [2, 0, 4]))#test correct handling of division per zero error  
             
        def testExponent (self):
            self.assertEqual ([2, 1, 1], exponent ([2, 4, 1], [1, 0, 5]))
            self.assertEqual ([16, -27], exponent ([2, -3], [4, 3, 5]))#test negative number
            self.assertEqual ([0.125], exponent ([2, 3], [-3]))#test negative exponent  and different size list        
  
        def testSquare (self):
            self.assertEqual ([4,36, 9], square ([2,-6, 3]))
            self.assertEqual ([16, 25], square ([4,-5]))
 
        def testSquareRoot (self):
            self.assertEqual ([2, 6, 3], squareRoot ([4, 36, 9]))
            self.assertEqual (['a negative number does not have a square root', 8, 7.21, 1], squareRoot ([-5, 64, 52, 1])) #test handling of square root of negative number error
            
        def testCube (self): #test combinaisons of negative and positive numbers
            self.assertEqual ([64,-8 ,-512, -1], cube ([4,-2 ,-8, -1]))

            
        def testFactorial (self):
            self.assertEqual ([24,-2 ,-24], factorial ([4,-2 ,-4])) #test combinaisons of negative and positive numbers
            self.assertEqual ([1], factorial ([0])) #test !0 

            
        def testCosinus (self):
            self.assertEqual ([-0.65,-0.99 ,-0.21], cosinus ([4,-3 ,4.5]))
            self.assertEqual ([1], cosinus ([0]))
 
#call function to launch tests
unittest.main()
#call main menu function
MainMenu()
