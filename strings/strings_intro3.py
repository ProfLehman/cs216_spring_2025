
# strings_intro3.py
# prof. lehman
# 2.14.2025
# in-class demos related to string functions
#

# return last space - using loop "old school" approach
#                     also if language has limited string functions
def lastSpace( temp ):
   
    p = len(temp)-1
    while p >= 0 and temp[p] != " ":
        p = p - 1
        #if p == -1:
        #    break

    return p

# return last space using rfind method
def lastSpaceAlternate( temp ):
    return temp.rfind(" ")
    
# return first space
def firstSpace( temp ):
    return temp.find(" ")

# return last name - using loop "old school" approach
#                     also if language has limited string functions
def lastName( temp ):
    result = ""
    
    p = lastSpace(temp) + 1
    
    while p < len(temp):
        result = result + temp[p]
        p = p + 1
    
    return result

# return last name using python functions
def lastNameAlternate( temp ):
    return temp[ lastSpace(temp)+1: ]


# return first name
def firstName( temp ):
    fs = firstSpace(temp)
    return temp[ 0:fs ]

# return middle initial
def middleInitial( temp ):
    return temp[ firstSpace(temp)+1 ]

# convert first middle last to last, first *using* helper functions
def lastFirst( temp ):
    
    lname = lastName( temp )
    fname = firstName( temp )
    minit = middleInitial( temp )
    
    result = lname + ", " + fname + " " + minit + "."
    result = result.lower()
    return result
  
# convert first middle last to last, first *without* using helper functions
def lastFirstAlternate( temp ):
    return (temp[temp.rfind(" ")+1:]+", "+temp[:temp.find(" ")]+" "+temp[temp.find(" ")+1]+".").lower()
    
# convert first middle last to last, first using single letter extraction [p]
# and len(string) function
# approach would work with almost any coding language
# note: approach assumes there is a first, middle, and last name with two spaces
def lastFirstAlternate2( temp ):
    result = ""
    
    # convert temp to lower case
    temp2 = ""
    p = 0
    while p < len(temp):
        if ord(temp[p]) >= 65 and ord(temp[p]) <= 90:
            # covert to lower case by adding 32
            temp2 = temp2 + chr(ord(temp[p])+32)
        else:
            temp2 = temp2 + temp[p]
        p = p + 1
        
    temp = temp2 #store lowercase version back in temp
    
    # find first space
    first_space = 0
    while temp[first_space] != " ":
        first_space = first_space + 1
    
    # find last space
    last_space = len(temp) - 1
    while temp[last_space] != " ":
        last_space = last_space - 1
        
    # add last
    p = last_space + 1
    while p < len(temp):
        result = result + temp[p]
        p = p + 1
    
    result = result + ", "
    
    # add first
    p = 0
    while p < first_space:
        result = result + temp[p]
        p = p + 1
    
    result = result + ", "
    
    # add middle
    result = result + temp[ first_space + 1 ]
    result = result + "."
    
    return result
    
    
# test lastSpace function
#                 012345678901234567
print( lastSpace("ALICE JOY ANDERSON") ) # 9
print( lastSpace("Norman The Forester") ) # 10
print( lastSpace("John Jacob Jigleheimer Schmidt") ) # 22
print( lastSpace("spring") ) # -1
print()

# test lastName function
print( lastName("ALICE JOY ANDERSON")) # ANDERSON
print( lastName("Norman The Forester") ) # Forester
print( lastName("John Jacob Jigleheimer Schmidt") )  # Schmidt
print()

# test lastFirst
print( lastFirst("ALICE JOY ANDERSON")) # anderson, alice j.
print( lastFirst("Norman The Forester") ) # forester, norman t.
print( lastFirst("John Jacob Jigleheimer Schmidt") ) # schmidt, john j.
print( lastFirst("Michael B. Jordan")) # jordan, michael b.
print()

# test altLastFirst
print( lastFirstAlternate2("ALICE JOY ANDERSON")) # anderson, alice, j.
print( lastFirstAlternate2("Norman The Forester") ) # forester, norman, t.
print( lastFirstAlternate2("John Jacob Jigleheimer Schmidt") ) # schmidt, john, j.
print( lastFirstAlternate2("Mike B. Jordan")) # jordan, mike, b.
print()







