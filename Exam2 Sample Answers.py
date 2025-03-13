#
# CS216 Exam #2
# spring 2025
# Lehman
# Sample Answers
#

#1 show output for the following:
s = "python"

print( s[2] )
print( s[0:3] )
print( s[:2] )
print( s[4:] )
print( s[-2] )
print()

#2
print( len(s) )
print( s.find("y") )
print( s.find("y", 2) )
print()

#3
print( s.capitalize() )
print( s.upper() )
print( s )
print()


#4 Given variables,
# Complete print statement such that the output will
# be as shown.  Code must work if product and price change.
# Price of iPhone Pro Max is $1199.9900
product = "iPhone Pro Max"

price = 1199.9900

print(f"Price of {product} is ${price:,.2f}" )
print()


#5. create a "stub" function called
# getPayment that takes an amount, rate, and years
# and returns the loan payment.  Use -1.0 as the
# default payment returned.
def getBMI( weight, height):
    result = -1.0
    
    return result

print( getBMI(160, 5.11) ) #displays -1.0
print()


#6. Complete function to return last name
#note: assume the name will have exactly one space between first and last
def getLastName( name ):

    # approach #1
    pos = name.find(" ") # find space
    last = name[pos+1:] # extract last name
    
    # approach #2 - with list split
    last = name.split(" ")[1]
    
    # approach #3 - use loop to find position of first space
    pos = -1
    i = 0
    while i < len(name):
        if name[i] == " ":
            pos = i
            break
        i = i + 1
        
    last = name[pos+1:] # extract last name   
    
    return last


    
print( getLastName( "Ada Lovelace" ) )  # Lovelace
print( getLastName( "Charles Babbage" ) )  # Babbage
print()


#7 Complete the function countletters that will return
#  the number of occurances of letter in name.
def countLetters( name, letter ):
    count = 0
    i = 0
    while i < len(name):
        if name[i] == letter:
            count = count + 1
        i = i + 1
        
    return count

#alternate one-line approach
def countLetters2( name, letter ):
    return name.count(letter)        

#alternate approach with in
def countLetters3( name, letter ):
    count = 0
    for n in name:
        if n == letter:
            count = count + 1
    return count

#alternate approach with find
def countLetters4( name, letter ):
    count = 0
    pos = name.find(letter, 0)
    while pos != -1:
        pos = name.find(letter, pos+1)
        count = count + 1
    return count

print( countLetters4("Charles Babbage", "b") ) #2
print( countLetters4("Apple Computer", "p") ) #3
print( countLetters4("Apple Computer", "x") ) #0
print()


#8 Complete the function displayReversed that will take a
# string and print the word in reverse order.
# Note: Python does not have a .reverse() or .reversed() method
def displayReversed( word ):
    i = len(word)-1
    while i >= 0:
        
        # only print if not a space
        if word[i] != " ":
            print( word[i], end="")
        
        # alternate approach to removing spaces
        #print( word[i].strip(), end="")
        i = i - 1
    print()

displayReversed("Ada Lovelace") #ecalevoL adA
displayReversed("Charles Babbage") #egabbaB selrahC
print()


#9 Given the following functions.  What will be display to the screen?
def changeIt( x ):
    x = -1

def changeList( list ):
    list[0] = -1
    
#*** main ***
x = 7
changeIt( x ) #7 no change x is not mutable
print( x )

y = 7
changeIt( y ) #7 no change y is not mutable
print( y )
print()

list = [2, 3, 4]
changeList(list) #list will change [-1, 3, 4] as list is mutable
print( list )
print()


#10 What will be displayed by the following?
list = [0] * 1000
print( len(list) )
print( list[0] )
print()

#Given given a list of exam scores
# note: assume the list contains int values that
# are in the range of 0 to 100
# ... indicates there are additional scores not shown.
exam = [77, 90, 54, 46, 94, 78]


#11 Show the code needed to change the 2nd
# score in the list to 91
exam[1] = 91
print( exam )
print()


#12 Show code needed to add the score
#   89 to the end of list
exam.append( 89 )
print( exam )


#13 Show code needed to remove the first score from the list
exam.pop(0)
print( exam )


#14 Show the code needed to sort the list
exam.sort()
print( exam )
print()


#15 Show the coded needed to display the lowest exam score
print( "Min = ", min(exam) )

# alternate approach - note: changes exam
exam.sort()
print( "Min = ", exam[0] )

# alternate approach
smallest = exam[0] #assume first is smallest
for score in exam:
    if score < smallest:
        smallest = score
print( "Min = ", smallest )
print()


#16 Show code needed to display all scores that
# 60 to 100

# using in
for e in exam:
    if e >= 60 and e <= 100:
        print( e )
print()

# using index
i = 0
while i < len(exam):
    if exam[i] >= 60 and exam[i] <= 100:
        print( exam[i] )
    i = i + 1
    
print()


#17 Show code needed to add +2 to all exam scores
i = 0
while i < len(exam):
    exam[i] = exam[i] + 2
    i = i + 1

print( exam )
print()


#18 Show code needed to create a dictionary of zipcodes with two initial values
# Huntington and 46750
# and Warren 46792
zip = { "Huntington":"46750", "Warren":"46792" }
print( zip )


#19 Show code to add Bippus and 46713 to the zip dictionary.
zip["Bippus"] = "46713"
print( zip )
print()


#20 Show code to input a City name, and display the zip code if the
#   the city is found in the dictionay, or "Not Found" if it is not in the dictionary.
city = input("Enter City: ")

print( zip.get( city, "Not Found" ) )

# alternate approach
if city in zip:
    print( zip.get(city) )
else:
    print( "Not found")

# alternate approach
if city in zip:
    print( zip[city] )
else:
    print("Not found")

# alternate approach
found = False
for c, z in zip.items():
    if city == c:
        found = True
        print( z )
        
if not found:
    print( "Not found" )
    
print()
print()


#21 Show code to display all zip codes stored in dictionary.
for z in zip.values():
    print( z )
print()

# alternate approach
for key in zip:
    print (zip[key])
print()

# alternate approach
for k,v in zip.items():
    print (v)
print()

# alternate approach
print( zip.items() )


#22 Show code to remove Warren from the dictionary
zip.pop("Warren")
print(zip)














