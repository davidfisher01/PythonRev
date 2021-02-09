from math import *    # imports math library


name = "John"
age = 35   # have to cast to string to concatenate
character_alive = True
print("Age: " + str(age) + "\n" + "Name: " + name)
# " to create a quotation in line,
# backslash means rendering literally for next character

# working with strings
print(name.lower())
print(name.upper())
print(len(name))
print(name[len(name) - 1])
print(name.index("n"))  # returns index of G
print(name.replace("John", "Elephant"))
# can use isupper or islower to check and return a boolean

# working with numbers
print(abs(age))   # absolute value
print(pow(3, 2))   # is 3^2 = 9
print(max(4, 6))   # returns higher num, can also use min
print(round(3.7))   # rounds number
print(floor(3.7))   # first number
print(ceil(3.7))    # rounds up no matter what
print(sqrt(age))

# Input from users
name = input("Enter in ur name: ")
print("Hello" + name + "!")
# inputs are automatically made as strings, so you have to cast
# them to doubles

# lists and list functions
friends = ["Kevin", "Karen", "Jim", 2, False, "Karen"]
nums = [4, 8, 15]
print(friends[0])
print(friends[-1])  # starts indexing from back of list
print(friends[1:])  # starts at 1 and goes to the end
print(friends[1:3]) # prints elements 1 & 2, not inclusive 3
friends[1] = "Mike"
friends.extend(nums)  # adds the nums list to friends
friends.append("Bob")  # adds friend onto end of list
friends.insert(1, "Steve")  # adds steve to index position 1
friends.remove("Jim")
friends.clear()       # empties list
friends.pop()         # removes last element off of list
friends.index("Kevin")  # gives Kevin's index
friends.count("Karen")  # counts # of Karen's
friends.sort()        # sorts list in ascending order(Strings or nums)
friends.reverse()    # reverses the order of list
friends2 = friends.copy()

# Tuples (soft brackets, immutable = can't be changed or modified)
coordinates = (4, 5)
print(coordinates[0])  # same indexing as lists
coordinates = [(4, 5), (5, 6), (9, 9)] # list of tuples

#check out how to make a dictionary object with a key and value in the Month Dictionary file

# functions
def say_hi(name):
    print("Hello" + name)


say_hi("kevin")   # calls function


def cube(n):
    return n*n*n


int = cube(2)

# if statements and comparisons
is_male = True
is_tall = False
if is_male or is_tall:
    print("ur a male")
elif is_male and not(is_tall):
    print("blah blah blah")
else:
    print("ur a female")
# for numbers all boolean operators apply

# while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# for loops
for letter in "Giraffe":
    print(letter)

for i in range(len(friends)):
    print(i)
for i in range(3,10):
    print(i)
# not inclusive for second variable in range

#exponenet function
print(2**3)
def raise_to_power(base_num, power):
    result = 1
    for i in range(power):
        result = result*base_num
    return result
raise_to_power(2,3)

#2D Lists
number_grid = [  # list has 4 rows and 3 columns
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0][0])
for row in number_grid:  # prints out every element in array
    for col in row:
        print(col)


# creating a student from the HowToMakeAClass file
# that shows you the actual format of how to make a class.
# Init here
from HowtoMakeAClass import Student
student1 = Student("Jim", "business", 3.1, False) # creates a student named Jim who is majoring in business, with a 3.1 GPA and isn't on probation
print(student1.name)   # prints out Jim
print(student1.gpa)  # prints out gpa
student2 = ("Pam", "art", 2.5, True)
print(student1.honorRoll) #executes the honorRoll function that I wrote in the class
#list of students, adding our 2 students
classroom = []
classroom.append(student1)
classroom.append(student2)






