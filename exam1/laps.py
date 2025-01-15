# laps.py
# in-class example
# spring 2025
# prof. lehman
#
# create an app that asks for the number of laps swam
# and displays the number of miles swam
#
# assume the pool is 25 meters long
# assume a lap is "down and back"

# input
laps = int( input("enter laps: ") )

# processing
meters = laps * 2 * 25
feet = meters * 3.28
miles = feet / 5280

# output
print()
print(f"{laps} laps = {miles:.2f} miles" )

"""
Sample Calculations
laps => miles
1 => .03
300 => 9.32 
16 => .50


Input Processing Output

Input
(laps)

Processing
(meters) = laps * 2 * 25  note: pool is 25 meters long
(feet) = meters * 3.28    note: 3.28 feet per meter
(miles) = feet / 5280     note: 5,280 feet in a mile

Output
miles use format "16 laps = .50 miles"

"""