# multiplicationTable.py
# prof. lehman
# spring 2025

# demonstrates nested loops
# comparing while vs. for
#
# note: these are examples
# of "count controlled" loops

# while loop approach
row = 0
while row <= 5:
    
    col = 0
    while col <= 5:
        answer = row*col
        print( f"{answer:4}", end="" )
        col = col + 1
        #while col
    
    print() #go to next line
    
    row = row + 1
    #end while row
    
print()
print()

# for loop approach
for row in range(0,6):
    for col in range(0,6):
        answer = row * col
        print( f"{answer:4}", end="" )
        
    print() #go to next line
    # end for col

# end for row

# -- end of program --
    
    
    