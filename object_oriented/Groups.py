import random

# -----------------------------------------------------------------------
#
#        file: Groups.py
#
#      Author: Prof. Lehman
#        Date: March 17, 2025
#
# Description: 'Groups' class holds list of students,
#               display_groups method randomlly assigns
#               students to a group.
#              
# -----------------------------------------------------------------------

class Groups:
    
    def __init__(self):
        self.students = []
    
    def add_student(self, name):
        self.students.append(name)
    
    def display_groups(self):
        random.shuffle(self.students)
        
        # create groups
        group = 1
        i = 0
        while i < len(self.students)-3:
            print( f"Group {group}: {self.students[i]}, {self.students[i+1]}")
            
            i = i + 2
            group = group + 1
            
        # handle last group
        if len(self.students)-2 == i:
            print( f"Group {group}: {self.students[i]}, {self.students[i+1]}")
        else:
            print( f"Group {group}: {self.students[i]}, {self.students[i+1]}, {self.students[i+2]}")
    
# Example usage
if __name__ == "__main__":
    
    sg = Groups()
    
    sg.add_student("Madelynn")
    sg.add_student("Jori")
    sg.add_student("Nathan")
    sg.add_student("Lukas")
    sg.add_student("Earl")
    sg.add_student("Grace")
    sg.add_student("Raymond")
    sg.add_student("Zen")
    sg.add_student("Jon")
    sg.add_student("Hannah")
    
    sg.display_groups()
