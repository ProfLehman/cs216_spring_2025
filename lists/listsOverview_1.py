import random

# listsOverview.py

# list similar to "array"
# set of consecutive memory locations
# work with "group" of variables or data

#create list with int values
a = [5, 3, 4, 7, 2, 1, 9, 2]

print( a ) #[5, 3, 4, 7, 2, 1, 9, 4, 4, 4]
print( len(a) ) #10
print( a[0] ) #5
print( a[1] ) #3
#print( a[10] ) # Error out of range


#print or get last item
print( a[-1] ) # 4
print( a[ len(a)-1 ] ) # 4
print()

print()

b = ["cake", "pie", "ice cream"]
print( b )
print( len(b) ) #3
print( b[1] ) #pie
print()


# cookies
cookies = ["thin mints", 100, "tag alongs", 50, "Samoas", 250]

print( len(cookies) )
print( cookies )
print()


f = 0
while f < len(cookies):
    print( f, ":", cookies[f] )
    f = f + 1
print()   


f = 0
while f < len(cookies):
    print( f, f+1, ":", cookies[f], "qty:", cookies[f+1] )
    f = f + 2
print()
print()

# parallel list
cookies = ["cookie one", "cookie two", "bob" ]
cookieQty = [ 2,              5, 6 ]

for i in range(0,len(cookies)):
    print( cookies[i], cookieQty[i] )



c = [78, 10, 20, 30, 40, 50, 60, 70, 90, 99, 98, 97, 96]

q = len(c)-1
while q >= 0:
    print( c[q] )
    q = q - 1
print()

exams = [78, 50, 60, 70, 5, 90, 80, 70, 6, 90, 90]
print( exams )

passing = 0
failing = 0
sum = 0

q = 0
while q < len(exams):
    
    if exams[q] >= 70:
        passing = passing + 1
        #print( exams[q] )
    else:
        failing = failing + 1
    
    sum = sum + exams[q]
    
    q = q + 1
    #end loop

avg = sum / len(exams)
print( "avg:", avg )
print( "passing: ", passing )
print( "failing: ", failing )

print

print( exams )

small = exams[0] #assume first is smallest
i = 1
while i < len(exams):
    if exams[i] < small:
        small = exams[i]
    i = i + 1
print( "small =", small )
print()

#d = [0,0,0,0,0,0,0,0,0,...]
MAX = 200

#print( "X" * 7 ) # XXXXXXX

flips = [0] * MAX #list of 200 ints

heads = 0
tails = 0

l = 0
while l < len(flips):
    flips[l] = random.randint(0,1)

    if flips[l] == 0:
        heads += 1
    else:
        tails += 1
        
    l = l + 1
 
print("heads ", heads)
print("tails ", tails)

print( flips  )

# number of times I flip three heads in a row?
count = 0
i = 0
while i < len(flips)-3:
    
    
    if flips[i] == 0 and flips[i+1] == 0 and flips[i+2] == 0:
        count = count + 1      
    
    i = i + 3
print( "x3 flips", count )







