# performance.java
# 3.15.2021 updated 2.25.2025
# prof. lehman
# demonstrates perfomance of list vs. dictionary search
# lists use sequential search O(N) - slow
# dictionaries use hash search O(1) - fast

import time


SIZE = 1000000

#**********************************************
# create list with values 0 to SIZE-1 
# and show time needed to find values in list
#**********************************************
list = [0] * SIZE
for i in range(0,SIZE):
    list[i] = str(i)

print(f"list size = {len(list):,d}")

print("Finding items in list...")
startTime = time.perf_counter()

#find i in list
count = 0
for i in range(0,SIZE,1000):
    if str(i) in list:
        count += 1

print( "count:", count )

stopTime = time.perf_counter()
elapsedTime = stopTime - startTime
print( "seconds:", elapsedTime )
print()
print()

#***************************************************
# create dictionary with values 0 to SIZE-1 
# and show time needed to find values in dictionary 
#***************************************************
dictionary = {}
for i in range(0,SIZE):
    dictionary[i] = str(i)
    
print(f"dictionary size = {len(dictionary):,d}")

print("Finding item in dictionary...")
startTime = time.perf_counter()

#find i in dictionary
count = 0
for i in range(0,SIZE,1000):
    if i in dictionary:
        count += 1

print( "count:", count )

stopTime = time.perf_counter()

elapsedTime = stopTime - startTime
print( "seconds:", elapsedTime )
print()
    