# Exam #3 Review - Page 2

class Coffee:
    
    def __init__(self, start_size="medium"):
        
        self.size = start_size
        
        
    def getPrice(self):
        
        price = 0.0
        
        if self.size == "small":
            price = 2.50
        elif self.size == "medium":
            price = 3.00
        else:
            price = 4.00
            
        return float(price)
    
    
    def setSize(self, new_size):
        
        if new_size == "small" or new_size == "medium" or new_size == "large":
            self.size = new_size
        
        
    def __str__(self):
        
        price = self.getPrice()
        return f"size: {self.size}, price: {price:.2f} "

# -- main --
myCoffee = Coffee()

print( myCoffee )
myCoffee.setSize( "mega grande super cup")
print( myCoffee )

myCoffee.setSize( "large")
print( myCoffee )

        