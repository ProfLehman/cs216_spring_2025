# ch1.py
# prof. lehman
# 1.13.2025
# zyBooks chapter 1 concept summary - with solutions

# output
print("text in double quotes")
print('text in single quotes')
print('be "consistent" with quotes')
print()

print("one") #advance to next line
print("two")
print("three", end="") #stay on line
print("four", end="")
print()
print()

#new line character \n
print("add line break here\ngo to second line")
print()

#variables
name = "Norman"     #string
age = 20            #int 
gpa = 3.87          #float
print( name )
print( name, age, gpa ) #adds space between
print()

#output variables and text
print( "Name is", name)
print( age, "years old, has GPA of", gpa)
print()

#input is string
name = input()
print("you entered:", name)
name = input("Enter your name: ")
print("you entered:", name)
print()

#int and float input must be converted
age = int( input("enter age in years: ") )
print( "In ten years you will be", age+10, "years old")
gpa = float( input("enter gpa: ") )
print( gpa )

# Does whitespace matter?
# Code density?

#input three numbers and print average
print("enter three numbers pressing <enter> after each number ...")

n1 = int(input())
n2 = int(input())
n3 = int(input())

avg = (n1 + n2 + n3) / 3.0

print("average is", avg)
print()

#? add message to each input
n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
n3 = int(input("Enter n3: "))

avg = (n1 + n2 + n3) / 3.0

print("average is", avg)
print()

#? make this a "one line" program
print((int(input("Enter n1: ")) + int(input("Enter n2: ")) + int(input("Enter n3: "))) / 3.0 )




