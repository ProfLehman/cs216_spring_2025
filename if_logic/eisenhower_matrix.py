# eisenhower_matrix.py
# 27 January 2025
#
# prof. lehman
#
# Implements the Eisenhower Matrix with individual if logic, elif logic
# and else if logic

# Input
print("Is the task important? (y/n)")
important = input().lower()  # convert input to lowercase for consistency

print("Is the task urgent? (y/n)")
urgent = input().lower()

print()
print()

# check for valid input
if (important == "y" or important == "n") and (urgent == "y" or urgent == "n"):
    pass  # continues without any output
else:
    print("Error: important and urgent must be 'y' or 'n'")
    print


# Processing: Individual If's
if important == "y" and urgent == "y":
    print("Quadrant 1: Do it now!")

if important == "y" and urgent == "n":
    print("Quadrant 2: Schedule it!")

if important == "n" and urgent == "y":
    print("Quadrant 3: Delegate it!")

if important == "n" and urgent == "n":
    print("Quadrant 4: Eliminate it!")


# Processing: if-elif-else logic
if important == "y" and urgent == "y":
    print("Quadrant 1: Do it now!")
elif important == "y" and urgent == "n":
    print("Quadrant 2: Schedule it!")
elif important == "n" and urgent == "y":
    print("Quadrant 3: Delegate it!")
elif important == "n" and urgent == "n":
    print("Quadrant 4: Eliminate it!")
else:
    print("Invalid input. Please enter 'y' or 'n' for both questions.")

    
# Processing: Nested if-else
if important == "y":
    if urgent == "y":
        print("Quadrant 1: Do it now!")
    else:
        print("Quadrant 2: Schedule it!")
else:
    if urgent == "y":
        print("Quadrant 3: Delegate it!")
    else:
        print("Quadrant 4: Eliminate it!")
        
print()
print()