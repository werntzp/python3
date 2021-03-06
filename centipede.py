"""
Centipede.py - Demonstrate various magic methods 
"""
class Centipede:
    
    # init internal lists 
    def __init__(self):
        self.__dict__["stomach"] = []
        self.__dict__["legs"] = []
    
    # append incoming value to internal list
    def __call__(self, *args):
        self.__dict__["stomach"].extend(args)

    # return inner list as comma separated string
    def __str__(self):
        return ",".join(self.stomach)

    # when setting new attributes, store that attribute name too
    def __setattr__(self, key, value):
        if key == "legs":        
            raise AttributeError("legs is for internal use only")
        elif key == "stomach":
            raise AttributeError("stomach is for internal use only")
        else:
            self.legs.extend([key])
            self.__dict__[key] = value

    # repr method returns attribute name list comma separated
    def __repr__(self):
        return ",".join(self.legs)


 
