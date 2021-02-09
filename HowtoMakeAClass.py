


class Student:

     def __init__(self, name, major, gpa, is_on_probation ):
         self.name = name
         self.major = major
         self.gpa = gpa
         self.is_on_probation = is_on_probation

     def honorRoll(self):
         if self.gpa >= 4.0:
             return True
         else:
             return False

