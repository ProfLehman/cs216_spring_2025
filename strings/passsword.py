
# password.py
# spring 2025
# prof. lehman
#
# in-class demo
#
# demonstrates use of sentinel loop,
# functions for organization,
# and string methods

# check password for 8+
def validLength( pw ):
    result = True
    
    if len(pw) < 8:
        result = False
        print("Error: need 8+ characters")

    return result

# check password for digit 0 to 9
def hasNumber( pw ):
    result = False
    
    # use while loop to get index of each letter
    i = 0
    while i < len(pw):
        
        #print( type(pw[i]) ) # display each letter
       
        # option #1 - could check for each digit
        # if pw[i] == "0" or pw[i] == "1" or pw[i] == "2" or pw[i] == "3" or pw[i] == "4" or pw[i] == "5" or pw[i] == "6" or pw[i] == "7" or pw[i] == "8" or pw[i] == "9":
       
        # option #2 - use in operator
        # if pw[i] in "0123456789":
        
        # option #3 - use python method isdigit()
        if pw[i].isdigit() == True:
            result = True
            
        i = i + 1
    
    if result == False:
        print("Error: need a digit 0 to 9")
        
    return result

# check for upper case letter
def hasUpperCase( pw ):
    result = False
    
    # use for loop with range to get index of each letter
    for i in range(0, len(pw)):
        
        if pw[i].isupper() == True:
            result = True
    
    if result == False:
        print("Error: need upper case letter")
        
    return result
    
# check for special character ie. any non-digit, non-letter, and not a space
def hasSpecial( pw ):
    result = False
    
    # get each letter using in operator ie. differs from using index
    for letter in pw:
        
        if letter.isalpha()==False and letter.isdigit() == False and letter != " ":
            result = True
    
    
    if result == False:
        print("Error: need special character (not number or letter or space)")
        
    return result   


# --- main ---
print("Must have 8 or more characters")
print()

valid = False

while valid == False:

    # get password to test
    print()
    password = input("Enter password: ")
    print()
    
    valid = True # assume true
    
    
    # password length
    if validLength( password ) == False:
        valid = False
        
    # password number
    if hasNumber( password ) == False:
        valid = False
    
    # upper case
    if hasUpperCase( password ) == False:
        valid = False
    
    # has special
    if hasSpecial( password ) == False:
        valid = False
        
    # end loop

# password is valid once exit loop
print()
print( f"Valid Password: {password}" )
    
    
    
    
