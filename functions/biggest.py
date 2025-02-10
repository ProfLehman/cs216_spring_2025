
# biggest.py
# spring 2025
# professor lehman
# four approaches for determining the biggest value

# determine biggest of three values
# scales well if additional arguments are added
def biggest_approach_1(a, b, c):
    big = a
    
    if b > big:
        big = b
        
    if c > big:
        big = c
        
    print( big )

# determine biggest of three values
# logic is straight forward
# will not scale as well as approach #1
def biggest_approach_2(a, b, c):
    
    if a > b and b > c:
        big = a
        
    elif b > a and b > c:
        big = b
    
    else:
        big = c
        
    print( big )

# determine biggest of three values
# logic works, but will not scale well
def biggest_approach_3(a, b, c):
    
    if a > b:
        if a > c:
            big = a
        else:
            big = c
    else:
        if b > c:
            big = b
        else:
            big = c
        
    print( big )

# determine biggest of three values
# using python built-in funciton max
def biggest_approach_4(a, b, c):
    
    print( max(a,b,c) ) #yes, that was easy

# --- main ---

# call function that does not return a value
biggest_approach_1(100, 50, 25 ) #100
biggest_approach_1(100, 150, 25 ) #150    
biggest_approach_1(100, 150, 250 ) #250
biggest_approach_1(50, 50, 50 ) #50
print()

biggest_approach_2(100, 50, 25 ) #100
biggest_approach_2(100, 150, 25 ) #150    
biggest_approach_2(100, 150, 250 ) #250
biggest_approach_2(50, 50, 50 ) #50
print()

biggest_approach_3(100, 50, 25 ) #100
biggest_approach_3(100, 150, 25 ) #150    
biggest_approach_3(100, 150, 250 ) #250
biggest_approach_3(50, 50, 50 ) #50
print()

biggest_approach_4(100, 50, 25 ) #100
biggest_approach_4(100, 150, 25 ) #150    
biggest_approach_4(100, 150, 250 ) #250
biggest_approach_4(50, 50, 50 ) #50
print()



