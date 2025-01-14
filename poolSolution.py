# poolSolution.py
# prof.lehman
# spring 2023
# determines the number of gallons needed to fill pool
# and number of trips needed

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

