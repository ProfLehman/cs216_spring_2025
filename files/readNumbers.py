# readNumbers.py
# spring 2025
# prof. lehman
# read from data file with one
# data item per line

# store sum of all numbers read
total = 0

# open file for reading
file = open("numbers.txt", "r")

# read first line  ie. priming loop
line = file.readline()

# process line until empty line read
# note: can also use while line
while line != "":
    
    number = int( line.strip() )  # or float(...)
    print( number )
    total = total + number
    
    # get next line
    line = file.readline()
 
 
print()
print( "Done reading file" )
print( f"total of numbers = {total:,d}" )

