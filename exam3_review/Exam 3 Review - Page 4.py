# Exam #3 Review - Page 4

with open("coins.csv", "r") as file:
    
    line = file.readline()
    
    while line != "":
        
        data = line.split(",")
        
        #print( data )
        
        price1 = float( data[1].strip() )
        price2 = float( data[2].strip() )
        
        if price2 > price1:
            print("***", data[0], "increased")
            
        line = file.readline()