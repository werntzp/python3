import re

def replace_digits(text):

    # don't forget to use a raw string constant!
    l = re.findall(r"\d{4}-\d{4}-\d{4}-\d{4}", text)
    for x in l:
        # do a substitution with last 4
        text = re.sub(x, "XXXX-XXXX-XXXX-" + x[-4:], text)
   
    # return out the new text
    return text

 
