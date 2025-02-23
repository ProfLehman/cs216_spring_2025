# listSearch.py
# prof. lehman
# spring 2024
# search for item in list

data = [ 2, 4, 5, 6 ]

print( 3 in data ) #False
print( 3 in data ) #True
print()

if 5 in data:
    print( "5 in data" )
else:
    print( "5 NOT in data" )
    
print()

# look for item in list with index
found = False
c = 0
while c < len(data) and found==False:
    if data[c] == 5:
        found = True #stops loop without break
    else:
        c = c + 1
    # end loop
    
if found == True:
    print( "yup, found 5" )
else:
    print( "did not find 5" )
    
    
    
        

        
        