# MooresLaw.py
# prof.lehman
# spring 2025
#
# in-class demonstration of using objects to
# solve problems
#
# class used to make Mooore's Law predictions

class MooresLaw:
    def __init__(self, year, value, unit):
        self.year = year      # e.g., 1971
        self.value = value    # e.g., 2300
        self.unit = unit      # e.g., "transistors"

    def __str__(self):
        return f"{self.year}: {self.value} {self.unit}"

    def predictFuture(self, years):
        current_year = self.year
        current_value = self.value
        print(f"{current_year}: {current_value} {self.unit}")

        elapsed = 0
        while elapsed + 2 <= years:
            elapsed += 2
            current_year += 2
            current_value *= 2
            print(f"{current_year}: {current_value} {self.unit}")

    def predictPast(self, years):
        current_year = self.year
        current_value = self.value
        print(f"{current_year}: {current_value} {self.unit}")

        elapsed = 0
        while elapsed + 2 <= years:
            elapsed += 2
            current_year += 2
            current_value *= 2
            print(f"{current_year}: {current_value} {self.unit}")

    def predictPast(self, years):
        current_year = self.year
        current_value = self.value
        print(f"{current_year}: {current_value} {self.unit}")

        elapsed = 0
        while elapsed + 2 <= years:
            elapsed += 2
            current_year -= 2
            current_value /= 2
            print(f"{current_year}: {current_value:.2f} {self.unit}")
        
    # alternate method uses predictFuture and predictPast
    def predict(self, years):
        if years >= 0:
            self.predictFuture( years )
        else:
            self.predictPast( years * -1 )
            
# -- end class --

# ** main **
memory = MooresLaw( 1996, 32, "MB" )

memory.predictFuture(10)
print()

memory.predictPast(10)
print()

memory.predict( 10 )
print()

memory.predict( -10 )
print()

phoneStorage = MooresLaw( 2025, 64, "GB" )
phoneStorage.predict( -10 )

