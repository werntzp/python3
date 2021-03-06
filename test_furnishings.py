"""
test_furnishings.py: verify you can add furnishings to a room and count them
"""
import unittest
from furnishings import *

class TestFurnishings(unittest.TestCase):
    
    def test_room(self):
        home = []
        home.append(Bed("Bedroom"))
        home.append(Sofa("Living Room"))
        d = map_the_home(home)
        self.assertEqual(2, len(d), "Should be two items in the dict!")
        b = home[0]
        self.assertTrue(isinstance(b, Bed), "When is a bed not a bed?")
        s = home[1]
        self.assertTrue(isinstance(s, Sofa), "Sofas not matching up!")
        
if __name__ == '__main__':
    unittest.main()

 
