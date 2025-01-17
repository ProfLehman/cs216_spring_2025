# Program Name: classStatus.py
# Date: January 17, 2025
# Author: Prof. Lehman
# Description: Determine class status based on hours completed
#              Demonstrates Individual and Nested If's
#              Note: assumes hours values will be valid


# Input
print("Enter hours completed: ")
hours = int(input())


# Individual If approach
#   each if statement operates independently
#   (-) Often less efficient
#   (+) May be easier to understand and avoid logic errors
#   (+) <= and >= easier to see numbers included
#       compared to < and >

status = ""

if hours <= 25:
    status = "Freshman"

if hours >= 26 and hours <= 55:
    status = "Sophomore"

if hours >= 56 and hours <= 85:
    status = "Junior"

if hours >= 86:
    status = "Senior"

print(f"Status is {status}")

# note: common error    => if hours >= 56 and <= 85:
#       repeat variable => if hours >= 56 and hours <= 85:

# note: python does allow => if 56 >= hours >= 85:

# If Else Nested If approach
#   all conditions are "linked"
#   (+) often more efficient ie. least number of comparisons
#   (-) may complicate logic
#   use of "if with else:" requires indenting as statements are nested
#     thus code can "drift" to right
status = ""

if hours < 26:
    status = "Freshman"
else:
    if hours < 56:
        status = "Sophomore"
    else:
        if hours < 86:
            status = "Junior"
        else:
            status = "Senior"

print(f"Status is {status}")


# elif Nested If approach (more compact form of if with else)
#   (+) allows all conditions to be left-aligned 
#         eliminating code "drift" to right
status = ""    

if hours < 26:
    status = "Freshman"
elif hours < 56:
    status = "Sophomore"
elif hours < 86:
    status = "Junior"
else:
    status = "Senior"

print(f"Status is {status}")


#Note: The following works but is NOT as efficient
#         as checking hours >= 26 and hours >=56 are not needed.
#           The only way to get to the second if is when hours
#             are already >= 26, checking is redundant
if hours < 26:
    status = "Freshman"
elif hours >= 26 and hours < 56:
    status = "Sophomore"
elif hours >= 56 and hours < 86:
    status = "Junior"
else:
    status = "Senior"
