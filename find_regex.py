"""
Regex class
"""

import re

class regex(object):

    inner = ("In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theory "
           "in a set of models using a notation called \"regular sets\" as a method to do pattern matching. Active "
           "usage of this system, called Regular Expressions, started in the 1960s and continued under such "
           "pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer.")

    def getmatchspan(self, phrase):
        m = re.search(phrase, self.inner)
        return m.span()

 
