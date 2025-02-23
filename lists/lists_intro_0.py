# file: lists_intro.py 
# name: *** add your name here ***
# date: 2.21.2025
# description: demonstrates basic functionality of a list


# +-----+
# |  1  |
# +-----+
#
# create list ** add five more values for a total of 10 numbers in list **
data = [87, 76, 92, 98, 84]

# display data
print( data )
print( f"Number of items in data = {len(data)}" )
print()

# display all data
i = 0
while i < len(data):
    print( data[i], end=" " )

    i = i + 1
    # end while

print()
print()
print()


# +-----+
# |  2  |
# +-----+
#
# ** update to also display the average **

# add all values in list
total = 0
i = 0
while i < len(data):
    total = total + data[i]

    i = i + 1
    # end while

print("Total", total)
print()
print()

# +-----+
# |  3  |
# +-----+
#
# ** update to also find and display the largest item number in the list **

# find smallest value
smallest = data[0] # assume first is smallest

i = 1 #note we start at 1 as we assume data[0] is smallest
while i < len(data):

    if data[i] < smallest:
        smallest = data[i]

    i = i + 1
    # end while

print( "Smallest is", smallest)
print()
print()

# +-----+
# |  4  |
# +-----+
#
# *** update to also display A 90 to 100 and C 70 to 79 counts **

# display all data bewteen 80 and 89
bCount = 0

i = 0
while i < len(data):
    if data[i] >= 80 and data[i] <= 89:
        bCount = bCount + 1

    i = i + 1
    # end while

print( "B Count:", bCount)
print()
print()

# -- end --