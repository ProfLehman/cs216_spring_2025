
# strings_first_middle_last.py
# prof. lehman
# in-class demo of string functions to extract
# first, middle initial, and last name

def firstName( temp ):
    return temp[ 0 : temp.find(" ") ]

def middleInitial( temp ):
    return temp[ temp.find(" ")+1 ]

def lastName( temp ):
    return temp[ temp.rfind(" ")+1: ]

def fullName( temp ):
    result = ""

    result += lastName(temp)
    result += ", "
    result += firstName(temp)
    result += " "
    result += middleInitial(temp)
    result += "."
    
    return result

   
#--- main ---
print( fullName("Augusta Ada King") )
print( fullName("William Henry Gates") )
print( fullName("Norman The Forester") )
print()

print( firstName("Norman The Forester") )
print( middleInitial("Norman The Forester") )
print( lastName("Norman The Forester") )

