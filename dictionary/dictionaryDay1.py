
# dictionaryDay1.py
# prof. lehman
# spring 2024
# demonstrates dictionary basics

# create an empty dictionary
cookie = {}   #dictionary

# display dictionary (will be empty)
print( cookie )

# add three key => value entries to dictionary
cookie[ "chocolate chip"  ] = 3
cookie[ "snickerdoodles"  ] = 12
cookie[ "oatmeal"  ] = 6

print( cookie )

# retrieve count
# key *must* be in dictionary, otherwise error
print( cookie["oatmeal"] )

# retrieve count, OK if not in dictionary
print( cookie.get("oatmeal") )
print( cookie.get("raisin") ) #None if not in dictionary
print( cookie.get("yucky", -1) ) # -1 if not in dictionary
print()

# search for item in dictionary
search = input("Enter cookie: ")

if search in cookie.keys():
#if cookie.get( search, -1) != -1:
#if cookie.get( search ) != None:
    print( "found" )
    print( cookie[search] )
else:
    print( "not found" )

# display all items in dictionary
print()
print("all items in dictionary")
for key, value in cookie.items():
    print( key, value )
print()

# display all keys in dictionary
print()
print("all keys in dictionary")
for key in cookie.keys():
    print( key )
print()

# display all values in dictionary
print()
print("all values in dictionary")
for value in cookie.values():
    print( value )
print()

# -- end --
