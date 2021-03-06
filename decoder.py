"""
decoder.py -- iterator that returns numbers 1-26 in list as letters
"""

class alphabator:
    def __init__(self, lst):
        "Initialize the iterator object."
        self.lst = lst
        self.itemno = 0
        self.count = 1
    def __iter__(self):
        "This object is not an iterable."
        return self
    def __next__(self):
        "Return the object in list, unless it is an integer between 1 - 26"
        if self.count > self.itemno:
            try:
                self.val = self.lst[self.itemno]
                # has to be an int
                if isinstance(self.val, int):
                    # check the range
                    if self.val in range(1, 27):
                        # tack on 96 to get to ascii letter we want and then uppercase 
                        self.val = chr(self.val + 96).upper()  
            except IndexError:
                raise StopIteration
            self.itemno += 1
            self.count += 1
        return self.val

    
