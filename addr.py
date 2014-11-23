"""
addr.py - Add various object types together
"""

def add_ints(o1, o2):
    """"
    Take two incoming objects, verify they are integers and add together if so
    """
    
    # verify both are ints and add them, if not, raise an error
    if isinstance(o1, int) and isinstance(o2, int):
        return int(o1) + int(o2)
    else:
        raise TypeError("Both objects not of type integer")
    

