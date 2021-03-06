"""
test_addr.py - Test add_ints() method from addr module
"""

import unittest
import addr 

class Test(unittest.TestCase):

    def test_add_ints_error(self):
        """
        Test raising errors when trying to add non-integer objects
        """
        self.assertRaises(TypeError, addr.add_ints, 1, "a")
    
    def test_add_ints_success(self):
        """
        Test adding two integers together
        """        
        self.assertEqual(addr.add_ints(1,1), 2, "Since when does 1+1 not equal 2? Stupid new math.")

if __name__ == "__main__":
    unittest.main() 
