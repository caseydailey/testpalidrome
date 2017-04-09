import unittest
#https://docs.python.org/3/library/unittest.html
from palindrome import Palindrome

#the class MUST start with 'Test'
class TestPalindrome(unittest.TestCase):

#defs must start with 'test_'
    def test_palindrome(self):
        pal = Palindrome()#create an instance of the Palindrome class object
        #run through a basic and edge cases of args
        self.assertTrue(pal.is_palindrome('level'))
        self.assertTrue(pal.is_palindrome('aredera'))
        self.assertFalse(pal.is_palindrome('potato'))
        #case sensitive
        self.assertFalse(pal.is_palindrome('LeVel'))
        #must have a length
        self.assertFalse(pal.is_palindrome(''))
        #can't just be a single letter (actuallly need to be 3 or more in def...)
        self.assertFalse(pal.is_palindrome('a'))
        #no nums
        self.assertFalse(pal.is_palindrome(131))
        self.assertFalse(pal.is_palindrome(tuple()))


if __name__ == '__main__':
    unittest.main()