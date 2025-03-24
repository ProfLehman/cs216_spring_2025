# writeCSV.py
# spring 2025
# prof. lehman
# write to .csv file

from random import *
import os

# open file for writting
file_name = "data.csv"
file = open(file_name, "w")

# write 50 rows of numbers
for i in range(0,50):
    
    label = "Row " + str(i)
    n1 = randint(0,2000)
    n2 = randint(0,2000)
    
    file.write( "{}, {}, {}\n".format(label,n1,n2) )
    print( "{}, {}, {}".format(label,n1,n2) ) #echo data written to file
    
file.close() #ensures file is written

# output number of bytes written
print()
bytes = os.path.getsize(file_name)
print("{} bytes written to {}".format( bytes, file_name) )
