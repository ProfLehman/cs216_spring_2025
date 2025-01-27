# sentinelLoop1.py
# prof. lehman
# spring 2025
# demonstrates "priming loop" approach to sentinel loops

# variables
total = 0    #store sum of all values
number = 0   #store number of values entered


# Sentinel loop

# initial input - "priming the loop"
print("Enter value (-1 to quit)")
value = int( input() )

while value != -1:
    
    if value > 10:
        print("Error")
    else:
        # value must be valid, thus add to totals
        number = number + 1
        total = total + value
    
    
    # repeat input
    print("Enter value (-1 to quit)")
    value = int( input() )
    
    #end while

# Output
print()
print( "number of values = ", number)
print( "total = ", total )