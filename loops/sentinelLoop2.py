# sentinelLoop2.py
# prof. lehman
# spring 2025
# demonstrates alternate approach to sentinel loops using
# stop value

# variables
total = 0    #store sum of all values
number = 0   #store number of values entered


# Sentinel loop
stop = False # ensures loop will execute at least one time

while stop == False:
    
    # input
    print("Enter value (-1 to quit)")
    value = int( input() )

    # process input
    if value == -1:
        stop = True # will stop loop when while is checked
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