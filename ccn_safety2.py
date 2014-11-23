import re

def replace_ccn(text):
    
    # compile a regular expression
    regex = re.compile(r"""
        \d{4}-  # 4 digits
        \d{4}-  # 4 digits
        \d{4}-  # 4 digits
        \d{4}   # 4 digits
        """, re.VERBOSE)

    # do a full substitution 
    return re.sub(regex, "CCN REMOVED FOR YOUR SAFETY", text)
   
