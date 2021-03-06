"""
furnishings.py: Creates furnishings object for a room 
"""
class Furnishing:
    def __init__(self, room):
        self.room = room
    
class Sofa(Furnishing):
    def __init__(self, room):
        super().__init__(room)
                
class Bookshelf(Furnishing):
    def __init__(self, room):
        super().__init__(room)
        
class Bed(Furnishing):
    def __init__(self, room):
        super().__init__(room)

class Table(Furnishing):
    def __init__(self, room):
        super().__init__(room)

def map_the_home(l):
    
    # empty dict that we'll use to store
    d = {}
    
    # walk through the list
    for i in l:
        # get the room name
        if i.room in d:
            objs = d[i.room]
            objs.append(i)
        else:
            objs = []
            objs.append(i)
            d[i.room] = objs

    return d

def counter(l):
    
    bed_ctr = 0
    bookshelf_ctr = 0
    sofa_ctr = 0
    table_ctr = 0 
    
    for x in l:
        if type(x) is Bed:
            bed_ctr += 1
        elif type(x) is Bookshelf:
            bookshelf_ctr += 1
        elif type(x) is Sofa:
            sofa_ctr += 1
        elif type(x) is Table:
            table_ctr += 1  
        
    print("Beds: " + str(bed_ctr))
    print("Bookshelves: " + str(bookshelf_ctr))
    print("Sofas: " + str(sofa_ctr))
    print("Tables: " + str(table_ctr))            

if __name__ == '__main__':
    home = []
    home.append(Bed("Bedroom"))
    home.append(Sofa("Living Room"))
    print(map_the_home(home))
    counter(home)


 
