# Referenced https://en.wikiversity.org/wiki/Python_Programming/Classes on 9/18/19
# Assignment 1 Part B for IT 310
# By Dyllan Sowers

# partB.py is a python class file for creating a shape object and outputting that shape's 
# perimeter and area. Each object has an inheritance structure, flowing down from the Polygon 
# object. Polygon has abstract methods perimeter() and area() which are used for calculating perimeter
# and area respectively. They are overrideen in cases for triangles and rectangles to use the appropriate 
# formula. 

# This program will prompt a user to enter a number, 0-8, corresponding to a shape on a printed
# menu in the console. The user will then be prompted to enter that shape's geometric properties 
# needed to calculate area and perimeter. These properties are stored in an array, 'sides' in the 
# Polygon parent class and fed into the classes with 'SideL' array from user input in the program body.

# After the results for one shape have been printed the user is prompted to choose to create another
# shape object. If the user enters 'n' the program will exit. 


# Each class name corresponds to the geometric shape it represents. s1, s2, s3, etc. correspond
# to each side input by the user for that object
class Polygon(object):
    sides = None    # empty sides array
    apothem = 1 # default to 1 to avoid divide by zero errors

    def __init__(self, sides, apothem): # constructor wil sides and apothem class variables
        self.sides = sides
        self.apothem = apothem
 
    def area(self): # default formaula for area of a regular polygon
        area = 0
        area = (float(self.apothem) * float(self.perimeter()))/2
        return area

    def perimeter(self): # formula used for perimeters of all shapes
        perimeter = 0 
        for side in self.sides:
            perimeter += float(side)
        return perimeter

class Triangle(Polygon): 
    height = 0

    def __init__(self, base, s2, s3, height):
        self.sides = [base, s2, s3]
        self.height = height

    def area(self): #overload the area method for triangles which don't always have an apothem
        area = 0
        area = .5 * float(self.sides[0]) * float(self.height)
        return area

class Quadrilateral(Polygon):
    def __init__(self, s1, s2, s3, s4, a):
        self.sides = [s1, s2, s3, s4]
        self.apothem = a

class Pentagon(Polygon):
    def __init__(self, s1, s2, s3, s4, s5, a):
        self.sides = [s1, s2, s3, s4, s5]
        self.apothem = a

class Hexagon(Polygon):
    def __init__(self, s1, s2, s3, s4, s5, s6, a):
        self.sides = [s1, s2, s3, s4, s5, s6]
        self.apothem = a

class Octagon(Polygon):
    def __init__(self, s1, s2, s3, s4, s5, s6, s7, s8, a):
        self.sides = [s1, s2, s3, s4, s5, s6, s7, s8]
        self.apothem = a

class IsoscelesTriangle(Triangle):
    def __init__ (self, s12, s3, height): #s12 are the equal length sides, s3 is the unequal
        self.sides = [s12, s12, s3]
        self.base = s3
        self.height = height

class EquilateralTriangle(Triangle):
    def __init__ (self, s123, height): #s123 is the equal length for all three sides
        self.sides = [s123, s123, s123]
        self.height = height

class Rectangle(Quadrilateral):
    def __init__(self, s13, s24): #s13 and s24 correspond to the opposing equal-length sides
        self.sides = [s13, s24, s13, s24]
    def area(self): # overload for rectangle area formula
        area = 0
        area = float(self.sides[0]) * float(self.sides[1])
        return area

class Square(Rectangle):
    def __init__(self, s1234): #s1234 is the euqal length of all 4 sides 
        self.sides = [s1234, s1234, s1234, s1234]

shapeOptions = ["Triangle", "Quadrilateral", "Pentagon", "Hexagon", "Octagon", "Isosceles Triangle"
, "Equilateral Triangle", "Rectangle", "Square"] # used for printing out options menu

while(True): # continue to prompt for shapes until user specified program exit
    optionCount = 0
    print("What type of shape would you like to create?\n\n The options are:")

    for shape in shapeOptions:
        print("Option", optionCount, ":", shape)
        optionCount += 1

    shapeNum = int(input("Select the number of the shape you want to create:\n"))
    sideL = []
    if(shapeNum >= 0 and shapeNum < 9): # give user confirmation for what object is selected
        print("You selected", shapeOptions[shapeNum])

    # Create the shape corresponding to the user's selection
    if (shapeNum == 0):
        for i in range(3):
            sideL.append(input("Enter side length (base first):\n"))
        sideL.append(input("Enter triangle height:\n"))

        shapeCreated = Triangle(sideL[0], sideL[1], sideL[2], sideL[3])

    elif(shapeNum == 1):
        for i in range(4):
            sideL.append(input("Enter side length:\n"))
        sideL.append(input("Enter apothem:\n"))

        shapeCreated = Quadrilateral(sideL[0], sideL[1], sideL[2], sideL[3], sideL[4])

    elif(shapeNum == 2):
        for i in range(5):
            sideL.append(input("Enter side length:\n"))
        sideL.append(input("Enter apothem:\n"))

        
        shapeCreated = Pentagon(sideL[0], sideL[1], sideL[2], sideL[3], sideL[4], sideL[5])

    elif(shapeNum == 3):
        for i in range(6):
            sideL.append(input("Enter side length:\n"))
        sideL.append(input("Enter apothem:\n"))

        shapeCreated = Hexagon(sideL[0], sideL[1], sideL[2], sideL[3], sideL[4], sideL[5], sideL[6])

    elif(shapeNum == 4):
        for i in range(8):
            sideL.append(input("Enter side length:\n"))
        sideL.append(input("Enter apothem:\n"))

        shapeCreated = Octagon(sideL[0], sideL[1], sideL[2], sideL[3], sideL[4], sideL[5], sideL[6], 
        sideL[7], sideL[8])

    elif(shapeNum == 5):
        sideL.append(input("Enter equal-length side length:\n"))
        sideL.append(input("Enter unequal-length side length:\n"))
        sideL.append(input("Enter height:\n"))

        shapeCreated = IsoscelesTriangle(sideL[0], sideL[1], sideL[2])

    elif(shapeNum == 6):
        sideL.append(input("Enter equal-length side length:\n"))
        sideL.append(input("Enter height:\n"))

        shapeCreated = EquilateralTriangle(sideL[0], sideL[1])

    elif(shapeNum == 7):
        sideL.append(input("Enter equal-length side length 1:\n"))
        sideL.append(input("Enter equal-length side length 2:\n"))

        shapeCreated = Rectangle(sideL[0], sideL[1])

    elif(shapeNum == 8):
        sideL.append(input("Enter equal-length side length:\n"))

        shapeCreated = Square(sideL[0])

    # if number is not correct ask to enter a correct one
    else:
        print("That is not a correct number! Please enter a number 0-8!")  
    
    # output perimeter and area using object methods
    if(shapeNum >= 0 and shapeNum < 9):
        print("Perimeter:", shapeCreated.perimeter(), "\nArea:", shapeCreated.area())

    another = input("Create another shape? (n to stop)\n") # continue to loop

    if (another == 'n'): # exit the program if the user enters 'n' 
        print("Thank you! Goodbye!")
        raise SystemExit
    



