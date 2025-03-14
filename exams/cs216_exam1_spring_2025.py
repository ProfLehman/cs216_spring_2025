# cs216 exam 1 - spring 2025
# sample answers
# prof. lehman

#1. What will be output by the following statements? (clearly show blank lines ie. “bl” if applicable)
print("A", end="")
print("B")
print("C\n")
print("D")
print()
print()

#2. What will be output by the following statements? (clearly show blank lines ie. “bl” if applicable)

A = 4
B = 2
print( "A + B" )
print( A * B )
print( A, B )
print( '"A", "B"')
print()
print()

#3.  Fill in the blank such that the message “Ticket for London is  $1,235.66” will be printed inserting the variables city and price. Must format price as currency with comma and 2 decimal places.
city = "London"
price = 1235.658

print( f"Ticket for {city} is ${price:,.2f}" )
print()
print()

#4. What will be output by the following statements?
x = 7
print( x % 5 )
x -= 1
print(x)      
x = 4**2
print(x)      
x = x / 2
print( x + 2 )
print()
print()

#5. What will be output by the following statements?
letter = "A"
gpa = 3.67
age = 18
print( type( letter ) )   
print( type( gpa ) )     
print( type( age ) )
print()
print()

#6. What will be output by the following statement?

print ( 40 + 50 / 5 * 5 + 10  )
print()
print()

#7.  (8 points) Fill in the blanks such that the numbers 100 down
# to 5 by 5’s ie. 100, 95, 85, … 10, 5,  will be printed to the screen.
# Use x as your counting variable and the print statement provided for your output.  
# You may not need to use all of the blanks.

x = 100

#while x >= 5:
while x != 5:

    print( x, end=", ")
    
    x = x - 5
   
#end loop
print()
print()

#8.  (6 points) Fill in the blanks such that the numbers 10 to
# 100 by 1’s ie. 10, 11, 12 … 99, 100, will be printed to the screen.
# Use x as your counting variable and the print statement provided for your output. 
#You will not need to use all of the blanks.
for x in range(10,101):

    print( x, end=", " )

    #end loop
print()
print()

#9
#9. (8 points) Show the statements needed to determine if the values entered for a and b are “all even”, 
#“all odd”, or “some even, some odd” displaying the appropriate message as as shown. You can assume the number entered will be a positive integer greater than zero.  You are given the code to input the values.

a = int(input())
b = int(input())

if a % 2 == 0 and b % 2 == 0:
    msg = "all even"
else:
    if a % 2 != 0 and b % 2 != 0:
        msg = "all odd"
    else:
        msg = "some even, some odd"

print( msg )
print()
print()

# 10. (16 points) Final Exams at ACME University are determined by the starting hour for the course as shown in the table below.  Write individual and nested if logic to determine the day based on the hour.
#
# hour        day
# 8, 9, 10 “Monday”
# 11, 12   “Wednesday”
# 1, 2, 3  “Friday”

hour = int( input() )
day = "unknown"

# 10a - Individual If
if hour >= 8 and hour <= 10:
    day = "Monday"
    
if hour == 11 or hour == 12:
    day = "Wednesday"

if hour >= 1 and hour <= 3:
    day = "Friday"

print("Day =", day)

day = "unknown" #reset day

# 10b - Nested If
if hour <= 3:
    day = "Friday"
elif hour <= 10:
    day = "Monday"
else:
    day = "Wednesday"
    
print("Day =", day)
print()
print()

#11.  What will be displayed by the following?

day = "Friday"
delay = False

time = "unknown"

if delay == True:
    time = "10:00 am"
else:
    if day == "Wednesday":
        time = "8:30 am"
    else:
        time = "8:00 am"

print( time ) 


#12.  How many times will “HU” be printed?  (Show your calculation) 3 x 4 x 2 = 24
count = 0
for i in range(0,3):
    for j in range(0,4):
        for k in range(0,2):
            #print("HU")
            count = count + 1
print( "HU printed ", count, "times" )

#13. What will be output by the following? (note: careful as this is slightly different than review example)

x = 1
while x <= 4:
    print( x, end=" " )
    if x == 3:
        break;
    else:
        x = x + 1
    #end loop

print( x )
print()
print()

#14. (10 points) Write a program that will input a number and print that number of asterisks across the screen as shown the sample runs.  You can assume the number will be 0 or higher.  Hint: use a loop

print("Enter Number")
number = int( input() )

count = 0
while count < number:
    print("*", end="")
    count = count + 1
    # end loop
    
print()
print()


#15. (16 points) Write a program that will input numbers as shown
#       until -1 is entered and then display the total for all numbers that are greater than or equal to 50 entered as shown.

# priming loop approach
total = 0

print("Enter Number: ")
n = int( input() )

while n != -1:
    
    if n >= 50:
        total = total + n
        
    print("Enter Number: ")
    n = int( input() )
    # end loop
    
print( "total", total )
print()

# break out approach
total = 0

while True:
    
    print("Enter Number: ")
    n = int( input() )

    if n == -1:
        break
    
    if n >= 50:
        total = total + n
        
    # end loop
    
print( "total", total )
print()
        
        
        
        
    
    
    








    
