# poolSolution.py
# prof.lehman
# spring 2023
# determines the number of gallons needed to fill pool
# and number of trips needed
#
# (*) see planning below

import math


# input
print("Enter pool length")
length = int(input())

print("Enter pool width")
width = int(input())

print("Enter pool depth")
depth = int(input())


# processing
volume = length * width * depth
gallons = volume * 7.5
trips = gallons / 4000
trips = math.ceil(trips)


# output
print()
print(f"A pool that is {length} feet in length,")
print(f"{width} feet in width,")
print(f"and {depth} feet in depth,")
print(f"will require {gallons:,.1f} gallons of water.")
print()

if trips <= 1:
    print("Only one trip is needed.")
    
if trips > 1:
    print(f"You will need {trips} trips.")


"""
-----------------------------------------------------------------------
 Sample Calculations and Expected Output

 Test your IPO plan by creating two (or more) sample calculations
 showing the inputs and expected outputs
 
 Key ideas are to verify that your IPO plan works
 *and* that you can test that your code works when it runs

 length, width, depth => gallons, trips
   20     10      6       9,000     3
   50     40      7      105,000    27
   10     4       2        600      1

-----------------------------------------------------------------------


 Input
    length of pool (length)
    width of pool (width)
    depth of pool (depth)

 Processing
    calculate the (volume) of the pool
       volume = length * width * depth
 
    calculate the (gallons) of water needed
       gallons = volume * 7.5

    calculate the number of (trips) given that a truck holds 4,000 gallons of water
       trips = gallons / 4000
       note: need to round up, so trips = math.ceil(trips)
    
    note: Use if statement determine if trips <= 1 or trips > 1

 Output
     (gallons) of water needed
     (trips) needed to fill pool
 -----------------------------------------------------------------------

"""