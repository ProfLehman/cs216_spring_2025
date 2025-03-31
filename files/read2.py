# read2.py
# spring 2021
# prof. lehman
# read from .csv data file
#     name,exam1,exam2
#     Alice,10,15

# open file
file = open("data2.csv", "r")

# read file into list
lines = file.readlines()

i = 0
while i < len(lines):
    #print( lines[i] )
    
    #create list from lines[i]
    data = lines[i].split(",")
    print( data )
  
    # get data fields
    name = data[0]
    exam1 = int(data[1])
    exam2 = int(data[2])
    
    #any processing here for one person
    # add to total, check for highest, etc..
    print(name, exam1, exam2)
    print()
    
    i = i + 1

print("Done reading file")
