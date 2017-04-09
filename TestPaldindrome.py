import unittest
from palindrome import Palindrome

class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        pal = Palindrome()
        self.assertTrue(pal.is_palindrome('level'))
        self.assertTrue(pal.is_palindrome('aredera'))
        self.assertFalse(pal.is_palindrome('potato'))
        self.assertFalse(pal.is_palindrome('LeVel'))
        self.assertFalse(pal.is_palindrome(''))
        self.assertFalse(pal.is_palindrome('a'))
        self.assertFalse(pal.is_palindrome(131))
        self.assertFalse(pal.is_palindrome(tuple()))


if __name__ == '__main__':
    unittest.main()