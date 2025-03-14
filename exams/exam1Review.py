# exam1Review.py
# spring 2025
# prof. lehman
# in-class review for CS216 Exam #1

#1 predict output
print("A")
print("B", end=" ")
print("C")
print("D")
print()
print()

"""
A
B C
D
"""

#2 predict output
print("A" + "\t", end="")
print("B" + "\n")
print("C")
print()
print()

"""
A <tab> B
<blank line>
C
"""

#side note regarding special characters and single and double quotes
print("'eh?'")
print('"eh?"')
print("\"eh?\"")
print("\\eh\\")
print()
print()

#3. formatted output: "cost of Tesla is $59,234.99"
item = "Tesla"
price = 59234.986

print( f"cost of {item} is ${price:,.2f}")
print()
print()

# other formatting place holders
# f float
# .2f float at two decimal
# x hex
# b binary
v = 17
print( f"{v} decimal = {v:b} binary = {v:X} hex")
w = "cold"
print( f"Today's word is {w}" )
print()
print()

#3
x = 7           #x:7    display:
print( x % 3)   #x:7    display: 1
x *= 2          #x:14   display:
#x = x * 2      #same as x *= 2
print( x )      #x:14   display: 14
x = x - 1       #x:13   display:
print( x ** 2 ) #x:13   display: 169
print( 6 / 2 * 3 + 6 )
print()
print()

# order of precedence ... /*  -+
x = 8 + 10 / 2
print( x ) #13    
#better to write as x = 8 + (10 / 2)
print()
print()

#5 while loop to print 10, 20, 30, 40, 50
x = 10
while x <= 50:
    print( x, end=", ")
    
    x = x + 10
    #end loop
    
print()
print()
    
#6
for x in range(10, 51, 10):
    print( x, end=", " )

print()

#alternate using list
for x in [10, 20, 30, 40, 50]:
    print( x, end=", " )

print()
print()

#7
number = int( input("Enter number: ") )
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
 
print()

# alternate approach (better as is separates msg from print)
if number % 2 == 0:
    msg = "even"
else:
    msg = "odd"

print(f"{number} is {msg}")
print()
print()


#8
qty = 7
price = 0

#individual if's
if qty == 1:
    price = 15.99
    
if qty >= 2 and qty <= 5:
    price = 14.99
    
if qty >= 6:
    price = 13.99
   
print( f"price = ${price:.2f}" ) 

price = 0

#nested elif's
if qty <= 1:
    price = 15.99
elif qty <= 5:
    price = 14.99
else:
    price = 13.99

print( f"price = ${price:.2f}" ) 

#nested else if's
if qty <= 1:
    price = 15.99
else:
    if qty <= 5:
        price = 14.99
    else:
        price = 13.99

print( f"price = ${price:.2f}" ) 
print()
print()

#9
total = 0
print("Enter number (-1 to quit)")
number = int( input() )

while number != -1:
    total = total + number
    
    print("Enter number (-1 to quit)")
    number = int( input() )
    #while
    
print("total", total)
print()
print()

#10
print("Enter password")   # priming the loop
password = input()
while password != "Norman":
    
    print("Wrong Password")
    
    print("Enter password")
    password = input()

print()
print()

#10 alternate approach #1
passwordOK = False
while passwordOK == False:
    
    print("Enter password")
    password = input()

    if password == "Norman":
        passwordOK = True
    else:
        print("Wrong Password")
        
    #end while
    
print()
print()
    
#10 alternate approach #2

while True:
    
    print("Enter password")
    password = input()

    if password == "Norman":
        break # breaks out of loop
    else:
        print("Wrong Password")
        
    #end while
    
print()
print()
    

#11
for i in range(0,5):
    for j in range(0,10):
        print("X", end=",")   #prints how many? 50
print()
print()
    
#12.
x = 65
print( x ) #65
print( chr(x) ) #A
print( str(x) ) #65
print()

y = "A"
print( ord(y) ) #65
print( type(y) ) #str

print()
print()

#13  displays: 0 1 2 3 4 5 5
x = 0
while x < 10:
    print( x, end=" " )
    if x == 5:
        break;
    x = x + 1
    #end loop
    
print( x )

 

# extra problem - print ASCII table
for letter in range(65,91):
    print( letter, chr(letter) )


# -- end review --
    