"""
test_coconuts.py - Test add_coconut and total_weight from coconuts module
"""

import unittest
import coconuts
from coconuts import Inventory, Coconut, AmericanCoconut, MiddleEasternCoconut, SouthAsianCoconut

class Test(unittest.TestCase):

    def test_coconut_weight(self):
        """
        Test coconut weights
        """      
        a = AmericanCoconut()
        s = SouthAsianCoconut()
        m = MiddleEasternCoconut()
        self.assertEqual(a.weight, 3.5, "American Coconut should be 3.5lbs!")
        self.assertEqual(s.weight, 3, "South Asian Coconut should be 3lbs!")
        self.assertEqual(m.weight, 2.5, "Middle Eastern Coconut should be 2.5lbs!")

    def test_add_coconut_error(self):
        """
        Test successfully adding a coconut to the iventory
        """
        
        # try to add a non-coconut object
        coconuts = Inventory()
        s = "Put the lime in the coconut"
        self.assertRaises(AttributeError, coconuts.add_coconut, s)
        
    def test_add_coconut_success(self):
        """
        Test raising AttributeError if a coconut object not used
        """        

        # create a coconut object
        coconuts = Inventory()
        c = AmericanCoconut()
        coconuts.add_coconut(c)
        self.assertEqual(coconuts.total_count(), 1, "Should only be 1!")

    def test_total_weight(self):
        """
        Test adding six coconuts together and returning correct weight
        """        
        coconuts = Inventory()
        c = SouthAsianCoconut()
        coconuts.add_coconut(c)
        coconuts.add_coconut(c)
        c = MiddleEasternCoconut()
        coconuts.add_coconut(c)
        c = AmericanCoconut()
        coconuts.add_coconut(c)
        coconuts.add_coconut(c)
        coconuts.add_coconut(c)
        self.assertEqual(coconuts.total_weight(), 19, "Coconuts do not add up properly!")
        
        

if __name__ == "__main__":
    unittest.main() 
