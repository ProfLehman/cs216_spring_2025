
# strings_intro2.py
# prof. lehman
# 2.14.2025
# in-class demos related to string functions
#

# return the left n characters
def left( text, n ):
    return text[0:n]
    #return text[:n]

# return the right n characters
def right( text, n ):
    #return text[ len(text)-n : len(text) ]
    #return text[ len(text)-n : ]
    start = len(text) - n
    stop = len(text)
    return text[ start : stop ]

# return middle n characters
def mid( text, start, n):
    return text[ start-1: start+n-1 ]


# ** main **
print( left("abcdefg", 2) ) # ab
print( left("huntington", 4) ) # hunt
#print( left("a",4) )
print()

print( right("abcdefg", 4) )  # defg
print( right("huntington", 3) ) # ton
print( right("a",4) ) # a
print()

print( mid("abcdefg", 2, 2) ) # bc
print( mid("abcdefg", 3, 4) ) # cdef
print( mid("huntington", 5, 3) ) # ing
print()


# find all of the a's using "old school" loop
#       012345
text = "Friday at 4pm Smith lecture at 4pm?"
i = 0
while i < len(text):
    if text[i] == "a":
        print( "a at", i )
    i = i + 1
print()

# find built-in string method
# find first four a's
pos1 = text.find("a") 
pos2 = text.find("a", pos1+1) #starts at pos1 + 1
pos3 = text.find("a", pos2+1)
pos4 = text.find("a", pos3+1) #note: -1 if not found
print("a at", pos1)
print("a at", pos2)
print("a at", pos3)
print("a at", pos4)
print()

# find all a's
text = "Will this find all of the a's maybe it will find all of the aaaas"
pos = text.find("a", 0)
while pos != -1:
    print( "a at", pos )
    pos = text.find("a", pos+1) # note we start looking just beyond where last was found
    
    
# there are other "high level" approachs in python
print()
positions = [index for index, char in enumerate(text) if char == 'a']
print(positions)  

for p in positions:
    print( "a at", p )
# -- end --
    














