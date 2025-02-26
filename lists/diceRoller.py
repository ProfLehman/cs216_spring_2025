
# diceRoller.py
# prof. lehman
# spring 2024
#
# demonstrates using list to store multiple counts

from random import *

# create list of 0's to hold counts
# set all counts to 0
# counts list stores dice rolls of 2 to 12
# note: list at index 0 and 1 not used
N = 12  
counts = [0] * (N+1) # 13 items indexed 0 to 12

print( counts )
print()

for i in range(0,100):
    
    # roll dice
    d1 = randint(1,6)
    d2 = randint(1,6)
    total = d1 + d2
    
    # update counts
    counts[total] = counts[total] + 1
    
    # end loop

# display counts
print()
print( counts )
print()
i = 2
while i < len(counts):
    print( f"number {i}'s = {counts[i]}" )
    i = i + 1
    
    
    
