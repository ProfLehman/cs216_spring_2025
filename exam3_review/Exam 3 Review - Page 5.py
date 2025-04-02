
# Exam #3 Review - Page 5

inventory = ["AWOL AT Guide 2023", 14.95, 20, "Darn Tough Socks", 23.00, 35, "MSR stove", 65.78, 15]

with open("inventory.csv", "w") as file:
    
    i = 0
    while i < len( inventory ):
        
        #print( inventory[i] )
        #print( inventory[i+1] )
        #print( inventory[i+2] )
        
        item = inventory[i] 
        price = inventory[i+1] 
        qty = inventory[i+2] 
        
        print( f"{item},{price},{qty}" )
           
        file.write( f"{item},{price},{qty}\n" )
        
        i = i + 3

