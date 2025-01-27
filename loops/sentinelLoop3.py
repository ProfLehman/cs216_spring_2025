# sentinelLoop3.py
# prof. lehman
# spring 2025
# demonstrates break approach to sentinel loops
#
# Note: Best to use breaks sparingly as they can 
#       lead to code with mutiple exit points that make
#       debugging difficult and could lead to logic errors
#
#       In the following example the loop exits from within
#       an if statement rather than the while condition.

# variables
total = 0    #store sum of all values
number = 0   #store number of values entered

# Sentinel loop
while True:
    
    # input
    print("Enter value (-1 to quit)")
    value = int( input() )

    # process input
    if value == -1:
        break # *** jumps out of loop ***
    elif value > 10:
        print("Error")
    else:
        # value must be valid, thus add to totals
        number = number + 1
        total = total + value
    
    #end while
    
# Output
print()
print( "number of values = ", number)
print( "total = ", total )