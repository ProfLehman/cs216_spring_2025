# readCSV.py
# spring 2025
# prof. lehman
# read from CSV file
#     label, number, number

# open file for reading
file = open("data.csv", "r")

# read first line  ie. priming loop
line = file.readline()

# process line until empty line read
# note: can also use while line
while line != "":

    # split line based on comma
    data = line.split(",")
    #print( data )
    
    # extract and convert data (ie. int and float must be converted)
    label = data[0].strip()
    n1 = int( data[1].strip() )
    n2 = int( data[2].strip() )
    print( f"{label}, {n1}, {n2}" )
           
    # read next line
    line = file.readline()
  
print()
print( "Done reading file" )