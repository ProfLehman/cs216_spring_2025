# writeNumbers.py
# spring 2025
# prof. lehman
# write numbers to text file
# one data item per line

from random import *
import os

# open file for writing
file_name = "numbers.txt"
file = open(file_name, "w") # w is for write mode

# write 50 numbers
for i in range(0,50):
    
    n = randint(0,2000) # get random number
    
    file.write( "{}\n".format(n) )
    print("{}".format(n)) #echo data written to file
    
file.close() #ensures file is written

# output number of bytes written
bytes = os.path.getsize(file_name)
print()
print("{} bytes written to {}".format( bytes, file_name) )



