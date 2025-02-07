# poolFunction.py
# prof.lehman
# spring 2023
# in-class example for IPO and sample calculations
# determines the number of gallons needed to fill pool
# and number of trips needed
# demonstrates use of functions

# -----------------------------------------------------------------------
# Input
#    length of pool (length)
#    width of pool (width)
#    depth of pool (depth)

# Processing
#    calculate the (volume) of the pool
#       volume = length * width * depth
#    calculate the (gallons) of water needed
#       gallons = volume * 7.5
#    calculate the number of (trips) given that a truck holds 4,000 gallons of water
#       trips = gallons / 4000
#       note: need to round up, so trips = math.ceil(trips)
#    Use if statement determine if trips <= 1 or trips > 1
# Output
#     (gallons) of water needed
#     (trips) needed to fill pool
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# Sample Calculations and Expected Output
# Test your IPO plan by creating two (or more) sample calculations
# showing the inputs and expected outputs
# Key ideas are to verify that your IPO plan works
#  *and* that you can test that your code works when it runs

# length, width, depth => gallons, trips
#   20     10      6       9,000     3
#   50     40      7      105,000    27
#   10     4       2        600      1
# -----------------------------------------------------------------------



import math

def volume(l, w, d):
    #print("*** hey, I am in the volume function ***")
    return l * w * d

def gallonsByVolume(v):
    return v * 7.5

def gallons(l, w, d):
    return volume(l,w,d) * 7.5

def trips(g):
    return g / 4000 

def tripsByTruck(gallons, capacity):
    return gallons / capacity

def tripsNeed(trips):
    if trips <= 1:
        print("Only one trip is needed.")
    else:
        print(f"You will need {trips} trips.")
    #end function     

def getLength():
    print("Enter pool length")
    tempLength = int(input())
    return tempLength

def getWidth():
    print("Enter pool width")
    temp= int(input())
    return temp

def getDepth():
    print("Enter pool depth")
    temp = int(input())
    return temp


def narrativeOutput( length, width, depth, gallons):
    print()
    print(f"A pool that is {length} feet in length,")
    print(f"{width} feet in width,")
    print(f"and {depth} feet in depth,")
    print(f"will require {gallons:,.1f} gallons of water.")
    print()
    
def shortOutput( length, width, depth, gallons):
    print( f"{length} {width} {depth} {gallons:,.1f}" )
    print()
    
    
    
# *** main ***

# input
length = 20  #getLength()
depth = 6   #getDepth()
width = 10  #getWidth()

# processing
gallons = gallons(length, width, depth)
trips = math.ceil( trips(gallons) )

# output
narrativeOutput(length, width, depth, gallons)
shortOutput(length, width, depth, gallons)

tripsNeed(trips)
