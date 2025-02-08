
# moduleB.py
# demonstrate how to import a module and call a function from it

# sample function
def msg():
    print("Today is Monday ...")

# prevent the code below from running when this module is imported
if __name__ == "__main__":
    print("Main from Module B")
    msg() # call the function from current module (ie. moduleB) 
    
    
    