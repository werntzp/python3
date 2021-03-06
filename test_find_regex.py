"""
Test regex matching
"""

import unittest
from find_regex import regex

class Test(unittest.TestCase):

    phrase = "Regular Expressions"

    def test_regex_span(self):
        """
        Test start and end position of pattern in the string
        """      
        r = regex()
        self.assertEqual(r.getmatchspan(self.phrase)[0], 231, "Wrong starting position!")
        self.assertEqual(r.getmatchspan(self.phrase)[1], 250, "Wrong ending position!")       

if __name__ == "__main__":
    unittest.main() 
