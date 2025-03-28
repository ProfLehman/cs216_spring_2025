# titanic.py
# prof. lehman
# in-class demo
# read titanic data file that is a CSV

# open file for reading
file = open("train.csv", "r")

# read headings 
first_line = file.readline()
print( first_line )


passenger_count = 0
lived = 0
died = 0

female_lived = 0
female_died = 0
male_lived = 0
male_died = 0


line = file.readline()

while line != "": 

    #print( line.strip() )
    
    # extract data
    data = line.split(",")  # creates a list called data
    #print (data)
    
    sex = data[5].strip() 
    
    survive = int( data[1].strip() )
    if survive == 1:
        lived = lived + 1
        
        if sex == "female":
            female_lived = female_lived + 1
        else:
            male_lived = male_lived + 1
    else:
        died = died + 1
        
        if sex == "female":
            female_died = female_died + 1
        else:
            male_died = male_died + 1
    
    
    passenger_count = passenger_count + 1
    
    line = file.readline()
    # end loop
    
print()
print("-- report --")
print( f"Passenger Count: {passenger_count}")
print( f"Lived {lived}, Died {died}")

print( f"Female Lived {female_lived}, Died {female_died}")
print( f"Male Lived {male_lived}, Died {male_died}")


file.close()
