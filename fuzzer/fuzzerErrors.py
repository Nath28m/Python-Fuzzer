# fusser error detection
import os
import subprocess
import sys

d_base = bytearray(b"AAAAAAAAAAAAAA") 
test = bytearray(b"\x18\x85\xff\xe0\x0f\xff") 
data_in = 'AAAAAAAAA'
for i in range (2**16): 
    d_vary = bytearray(i.to_bytes(2, byteorder='big')) 
    for index, value in enumerate(d_vary):
        if value == 0:
            d_vary[index] += 1
    data_in = d_base + d_vary + test 
    out = subprocess.run(['(./location)', bytes(data_in)], stdout=subprocess.PIPE) # run the program
    if out.returncode == -11: # -11 is the return code for a seg fault
        print("Error detected at: ", i)
        break
