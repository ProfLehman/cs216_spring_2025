# rightTriangle.py
# prof. lehman
# 1.29.2025
#
# uses three nested loops to calculate
# all pythagorean triples or "right triangles"
#
# demonstrates nested while vs. nested for loops
#

print("Enter N")
N = int( input() )

print(f"Requires {N**3:,d} iterations through loops")
print()

# while loop approach
count = 0
a = 1
while a <= N:
    b = 1
    while b <= N:
        c = 1
        while c <= N:
            if (a * a + b * b) == c * c:
                print(a, b, c)
                count = count + 1
            c += 1
        # end loop c
        
        b += 1
        # end loop b
        
    a += 1
    # end loop a

print()
print(f"count of triples {count:,d}")
print()

# for loop approach
count = 0
for a in range(1,N+1):
    for b in range(1,N+1):
        for c in range(1,N+1):
            if (a*a + b*b) == c*c:
                print( a, b, c )
                count = count + 1
            #end for c
        #end for b
    #end for a

print()
print(f"count of triples {count:,d}")
print()