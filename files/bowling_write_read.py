
# bowling_write_read.py
# prof. lehman
# March 31, 2025

# code demos creating CSV and reading from CSV file
# uses a dictionary to help calculate high scores
#
# code demonstrates "with" approach, thus file close is
# handled automatically


# *** step 1 ***
# Create scores.csv file

# open file for writing
file_name = "scores.csv"

with open(file_name, "w") as file:

    file.write("name, score\n")

    # get name
    name = input("Enter bowler name: ")

    while name != "stop":
        
        # get score
        score = int( input("Enter bowler score: ") )
        
        # write score to file
        print( name, score ) #echo to screen
        file.write( f"{name}, {score}\n" )
        
        # get name
        name = input("Enter bowler name: ")

        # end loop

print()

# step 2 - read file
# read scores.csv file and create high_score dictionary

high_score = {} # dictionary

# open file for reading
with open("scores.csv", "r") as file:

    # get headings and ignore
    line = file.readline()

    # read first line  ie. priming loop
    line = file.readline()

    # process line until empty line read
    # note: can also use while line
    while line != "":

        # split line based on comma
        data = line.split(",")
        #print( data )
        
        # extract and convert data (ie. int and float must be converted)
        name = data[0].strip()
        score = int( data[1].strip() )
        print( f"{name}, {score}" )
        
        if name in high_score:
            # have seen name, so get score and update if higher
            current_score = high_score[ name ]
            if score > current_score:
                high_score[ name ] = score 
        else:
            high_score[ name ] = score  # first time see name, store score
               
        # read next line
        line = file.readline()
        
        # end loop
        
print()
print( "Done reading file" )


# display all scores
print("All high scores")
for key, value in high_score.items():
    print( key, value )
print()

# sort scores
# high_scores.items() gives a list
# key = ... specifies sorting by the second item in list
# reverse = True specifies reverse order
top_three = sorted(high_score.items(), key=lambda item: item[1], reverse=True)

print("All high scores - Sorted")
for line in top_three:
    print( line[0], line[1] )
    
print()
print("Top 3")
for line in top_three[:3]:
    print( line[0], line[1] )

# note: does not handle "ties"















