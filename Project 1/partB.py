# Referenced https://en.wikiversity.org/wiki/Python_Programming/Classes on 9/18/19
# Assignment 1 Part B for IT 310
# By Dyllan Sowers

class Polygon(object):
    sides = None    
    apothem = 1 #default to 1 to avoid divide by zero errors

    def __init__(self, sides, apothem):
        self.sides = sides
        self.apothem = apothem

    def area(self):
        area = 0
        area = (apothem * perim)/2

    def perimeter(self):
        perimeter = 0
        for side in self.sides:
            perimeter += side
        return perimeter

class Triangle(Polygon):
    height = 0

    def __init__(self, base, s2, s3, height):
        self.sides = [base, s2, s3]
        self.height = height

    def area(self): #overload the area method for triangles which don't always have an apothem
        area = 0
        area = .5 * self.sides[0] * self.height
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
        self.apothem

class IsoscelesTriangle(Triangle):
    def __init__ (self, s12, s3, height): #s12 are the equal length sides, s3 is the unequal
        self.sides = [s12, s12, s3]
        self.base = s3
        self.height = height

#This is not a member of the triangle class since the formula for calculating the area of an 
#Equilateral triangle is not 1/2 b * h, it matches that of any regular polygon. 
class EquilateralTriangle(Polygon):
    def __init__ (self, s123, a): #s123 is the equal length for all three sides
        self.sides = [s123, s123, s123]
        self.apothem = a

class Rectangle(Quadrilateral):
    def __init__(self, s13, s24): #s13 and s24 correspond to the opposing equal-length sides
        self.sides = [s13, s24, s13, s24]
        self.apothem = a

class Square(Quadrilateral):
    def __init__(self, s1234): #s1234 is the euqal length of all 4 sides 
        self.sides = [s1234, s1234, s1234, s1234]
    def area(self):
        area = 0
        area = s1234 * s1234
        return area



