import random

# listProcessing.py
# prof. leheman
# spring 2024
#
# demonstrates list processing for one
# and two dimentional (ie. nested) lists

# list
numbers = [5, 4, 3, 2, 1]

# high-level functions
print( "sum", sum(numbers) )
print( "min", min(numbers) )
print( "max", max(numbers) )
print()

# add end
numbers.append( 6 )
print( numbers )

#add front
numbers.insert( 0, 7 )
print( numbers )

# add middle
numbers.insert( 3, 16 )
print( numbers )

# remove last
numbers.pop()
print( numbers )

# remove a number in the list
numbers.remove(16) #removes #
print( numbers )

# remove the first
numbers.pop(0)
print( numbers )
print()
print()

# set a value
numbers[1] = 99
print( numbers )
print()

# sort ascending
numbers.sort()
print( numbers )

# sort descending
numbers.reverse()
print( numbers )
print()

# process list with index - traditional
print("display list with index")
for i in range(0, len(numbers)):
    print( f"numbers[{i}] is {numbers[i]}" )
    numbers[i] = numbers[i] + 1
    
print()
print( numbers )
print()


# process list with "in"
print("display list with in")
for item in numbers:
    print( f"Next item is {item}" )
    item = -1  #does not change the list
    
print()
print( numbers )
print()

# process list with enumerate
print( "display list with enumerate" )
for index, value in enumerate(numbers):
    print( f"numbers[{index}] is {value}" )
    value = 6 #does not change the list
    numbers[index] += 1
    
print()
print( numbers )
print()
print()

# two dimensional array
# also called "nested" lists
grid = [[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

numRows = len(grid)
numCols = len(grid[0])
print( "rows", numRows )
print( "cols", numCols )
print()

#place 9's in random locations
count = 0
while count < 4:

    #get randdom row and column
    randomRow = random.randint(0,numRows-1)
    randomCol = random.randint(0,numCols-1)
    #print( randomRow, randomCol)

    # place if not duplicate
    if grid[ randomRow][ randomCol ] != 9:
        grid[ randomRow][ randomCol ] = 9
        count = count + 1


# display nested lists (ie. two dimensional array) - traditional
print( "display nested list with index" )
for r in range(0, len(grid)):  
    for c in range(0, len(grid[r])):  
        print( grid[r][c], end=" " )
    print()
print()

# display nested lists (ie. two dimensional array) - IN
print( "display nested list with in" )
for row in grid:
    for item in row:
        print( item, end=" " )
    print()
print()
    
# display nested lists (ie. two dimensional array) - enumerate
print( "display nested list with enumerate" )
for r, row in enumerate(grid):
    for c, item in enumerate(row):
        print( item, end=" " )
    print()




