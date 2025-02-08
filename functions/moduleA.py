# moduleA.py
# demonstrate how to import a module and call a function from it

# import the moduleB.py file
import moduleB

# sample function
def msg():
    print("Spring is coming!!!")

# prevent the code below from running when this module is imported
if __name__ == "__main__":
    print("Main from Module A")
    msg() # Call the function from moduleA   
    moduleB.msg() # Call the function from moduleB
    
    
    