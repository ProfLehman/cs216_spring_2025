# strings_intro1.py
# prof. lehman
# 2.12.2025
#
# revised by ___*** add your name ***
#
# virtual class demos related to string functions
#
#
# for class attendance
#
#   (1)update each of the strings
#
#   test and test2 in repeating text
#   s in "slicing and dicing"
#   day in "iterating through string"
#   word in "functions - removing vowels"
#
#   (2) run your code and update the comments
#       to show the actual output
#
#   (3) add your name to the comments and upload
#       revised strings_intro1.py to Moodle
#

# +-------------------------------
# | repeating text
# +-------------------------------
print("+------------------------------------+")

print( "Wednesday " * 5 ) # Wednesday Wednesday Wednesday Wednesday Wednesday
print()

test = "spring break " * 3  
print( test ) # spring break spring break spring break
print()

test2 = "fun "
print( test2 * 4 ) # fun fun fun fun
print()
print()


# +-------------------------------
# | slicing and dicing
# +-------------------------------
print("+------------------------------------+")

#    0123456
s = "abcdefg"

print( s[1] ) #b
print( s[0] ) #a
print( s[6] ) #g
#print( s[7] ) # error out of range
print()

print( s[1:3] ) #bc   string[start:stop+1]
print( s[3:6] ) #def
print( s[1:4] ) #bcd
print()

print( len(s) ) #7
print( s[0:len(s)] ) #abcdefg
print( s[0:] ) #abcdefg
print()

print( s[:3] ) #abc
print()

print( s[:] ) #abcdefg
print( s ) #abcdefg
print()

print( s[-1] ) #g
print( s[-2] ) #f
print()

#last three letters?
print( s[-3:] ) # efg
print( s[-3:len(s)] ) #efg
#print( "test", s[-3:0 ] )  # does not work must be low to high
#print( "test2", s[-3:-7] ) # does not work must be low to high
print()


#     0123456
#s = "abcdefg"
print( "first:", s[:1] ) #a
print( "all:", s[:] ) #abcdefg  
print()
print( "skip 2:", s[0:len(s):2] ) #aceg  skip every 2nd letter
print( "reverse:", s[::-1] )  # gfedcba
print()

#    0123456
#s = abcdefg
print( "last letter:", s[-1] ) # g
print( "last two letters:", s[-2:] ) #fg
print()
print()

# +-------------------------------
# | iterating through string 
# +-------------------------------
print("+------------------------------------+")

#      012345678
day = "wednesday"

# iterating through string - displays g[0]: w ... g[8]: y
g = 0
while g < len(day):
    print( f"g[{g}]: {day[g]}" )
    g = g + 1
  
print()

# iterate through string in reverse using loop - displays yadsendew 
g = len(day)-1
while g >= 0:
    print( day[g], end="" )
    g = g - 1
print()   
print()

# interate through string using for and range - prints wednesday
for i in range(0,len(day)):
    print( day[i], end="")
    
print()
print()

# iterate through string using for and in - prints wednesday
for letter in day:
    print( letter, end="" )
    
print()
print()

# function to reverse a string using a loop
def reverse( temp ):
    result = ""
    
    i = len(temp)-1
    while i >= 0:
        result = result + temp[i]
        i = i - 1
        
    return result

print( reverse(day) ) # yadsendew
print()
print( reverse("norman") ) # namron
print( reverse("forester") ) # retserof
print()



print()
print()

# +-------------------------------
# | functions - removing vowels
# +-------------------------------
print("+------------------------------------+")

# returns true if not a vowel
def notVowel( letter ):
    result = True

    letter = letter.lower()
    
    if letter == "a" or letter == "e"  or letter == "i" or letter == "o" or letter == "u":
        result = False
        
    return result

# return string with vowels removed
def removeVowels( temp ):
    result = ""
    
    i = 0
    while i < len(temp):
        if notVowel( temp[i] ):
            result = result + temp[i]
        i = i + 1
        
    return result

# test removeVowels function
print( removeVowels("norman") ) #nrmn
print( removeVowels("forester") ) #frstr
print()

word = "Computer"
print( removeVowels(word) ) #Cmptr
print()

print( removeVowels("It is amazing what you can read without vowels") ) #t s mzng wht y cn rd wtht vwls
print()








