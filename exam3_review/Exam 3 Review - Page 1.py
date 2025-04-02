
# Exam #3 Review - Page 1

class Employee:

    def __init__(self, name="unknown", year=2023):
        
        self.name = name  #instance variables
        self.year = year
    
    def set_year(self, temp_year):
        
        if temp_year >= 1982:
            self.year = temp_year
        else:
            print("Error: invalid start year, must be 1982+")
        
    def __str__(self):
        
        return f"Name: {self.name}, Year Hired: {self.year} "
    
# -- main --
alice = Employee("Alice Anderson", 2020)

bob = Employee()

print( alice.year )
print( bob.year )

bob.year = 2022
print( bob.year )
print()

print( alice )
print( bob )
print()

bob.name = "Robert Brown"
print( bob )
print()

bob.set_year(1776) # use method call to set year
bob.set_year(1999)

print( bob )
print()

