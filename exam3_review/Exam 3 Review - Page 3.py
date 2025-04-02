
# Exam #3 Review - Page 3

total = 0

# read items.txt
with open("items.txt", "r") as file:
    
    item = file.readline()
    
    while item != "":
        
        ounces = float( file.readline() )
        total = total + ounces
        
        print( item, ounces )
        
        item = file.readline()
        #while

print()
print("total", total)



