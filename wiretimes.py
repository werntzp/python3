"""
wiretimes.py: open Wireshark bin file to print timestamps
"""

import os, struct
from datetime import datetime

f = r"v:\workspace\Python3_Homework08\src\wireshark.bin"

# read entire file
d = open(f, "rb").read()  

# grab the magic number (tells us byte order and actual packets
magic = d[:4]                     
packets = d[24:]                     

# use magic to get byte order
o = struct.unpack('>L', magic)[0]
if o == 0xa1b2c3d4:
    order = '>'
elif o == 0xd4c3b2a1:
    order = '<'

packet_num = 1

while True:

    # get the first packet header, pull out timestamps and length
    try:
        sec, micro, ilen, olen = struct.unpack("{0}llll".format(order), packets[:16])

        print("======================")
        print("packet:",  packet_num)
        print(datetime.fromtimestamp(sec))
        print(int(micro))
        
        # use len to jump to new packet
        packets = packets[16 + ilen:]
        packet_num += 1
    
    except:
        break
     
