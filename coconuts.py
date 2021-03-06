"""
coconuts.py - Inventory class that tracks types of coconuts
"""

class Coconut(object):
    pass

class AmericanCoconut(Coconut):
    
    def __init__(self):
        self.name = "American"
        self.weight = 3.5

class SouthAsianCoconut(Coconut):
    
    def __init__(self):
        self.name = "South Asian"
        self.weight = 3
        
class MiddleEasternCoconut(Coconut):
    
    def __init__(self):
        self.name = "Middle Eastern"
        self.weight = 2.5

class Inventory:

    def __init__(self):
        self.cnuts = []
        
    def remove_all(self):
        """
        Remove all the coconuts from the inventory
        """      
        self.cnuts.clear()

    def add_coconut(self, c):
        """
        Add a coconut to the inventory
        """       
        # verify we have a Coconut class coming in
        if isinstance(c, Coconut):
            self.cnuts.append(c)    
        else:
            raise AttributeError("Can only add a coconut to the inventory!")
    
    def total_weight(self):
        """
        Return weight of all the coconuts
        """ 
        w = 0  
        for c in self.cnuts:
            w += c.weight
        return w
    
    def total_count(self):
        """
        Return number of coconuts in inventory
        """
        return len(self.cnuts)    
     
