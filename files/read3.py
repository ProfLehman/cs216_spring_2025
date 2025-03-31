# read3.py
# spring 2024
# prof. lehman
# read from .csv data file using csv.reader
#     name,exam1,exam2
#     Alice,10,15

import csv

# use csv reader
with open('data2.csv', 'r') as csvfile:
    
    data_reader = csv.reader(csvfile, delimiter=',')

    for row in data_reader:

        # row is a list
        print( row )
      
        # get data fields
        name = row[0]
        exam1 = int(row[1])
        exam2 = int(row[2])
        
        #any processing here for one person
        # add to total, check for highest, etc..
        print(name, exam1, exam2)
        print()

print("Done reading file")
