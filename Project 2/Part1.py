# Part1.py for IT310 Fall 2019, Professor Suboh Alkushayni
# By Dyllan Sowers and Ethan Curley

# The goal of this program is to compare timings of the sorting algorithms 
# Selection, Insertion, and Bubble Sort for sorting same-size lists of integers
# and fraction objects. The program consists of 3 main parts: the sort object, the
# Fraction object, and functions. Each section has its own subsequent description. 
# A function is included to export these timing results as a comma separated list.

import time
import random

# Create a Sort object used to sort a list and calculate sorting time. The object is 
# initiated with a list as a class variable, either a list of Fraction objects or integers. 
# The timings are  then stored in a class variable. Methods are included to return the contents
# of the list as a readible string and the sort timing. 

class Sort(object):
    numbers = [] # list to sort
    elapsedTime = 0 # elapsed time to sort list

    def __init__(self, numList): # Initiate with a list and assign variables
      self.numbers = numList
      self.numbersSize = len(self.numbers) # Size of list needed for algorithms

    def SelectionSort(self): # Selection Sort Algorithm. Sorts ascending.
       i = 0
       j= 0
       indexSmallest = 0
       temp = 0   
       startTime = time.time()

       for i in range(0, self.numbersSize):
           indexSmallest = i
           for j in range(i+1, self.numbersSize):
             if  self.numbers[j] < self.numbers[indexSmallest]:
                indexSmallest = j
         
           temp = self.numbers[i]
           self.numbers[i] = self.numbers[indexSmallest]
           self.numbers[indexSmallest] = temp
       endTime = time.time()
       self.setTime(startTime, endTime)


    def InsertionSort(self): # Insertion Sort Algorithm. Sorts ascending.
        i = 0
        j = 0
        temp = 0
        startTime = time.time()
        for i in range(1, self.numbersSize):
            j = i
            while j > 0 and self.numbers[j] < self.numbers[j - 1]:
                temp = self.numbers[j]
                self.numbers[j] = self.numbers[j - 1]
                self.numbers[j - 1] = temp 
                j -= 1
        endTime = time.time()
        self.setTime(startTime, endTime)
 
    def BubbleSort(self): # Bubble Sort Algorithm. Sorts descending. 
        startTime = time.time() 

        for i in range(0, self.numbersSize - 1):
            for j in range(0, self.numbersSize - i - 1):
                if self.numbers[j] > self.numbers[j + 1]:
                    temp = self.numbers[j]
                    self.numbers[j] = self.numbers[j + 1]
                    self.numbers[j + 1] = temp
        endTime = time.time()
        self.setTime(startTime, endTime)

    def setTime(self, startTime, endTime): # Update the elapsed sorting time variable.
        self.elapsedTime = endTime - startTime

    def getTime(self): # return the elapsed time as a string
        return str(self.elapsedTime) 

    def getList(self): # return the list as a string separated by , 
        return ', '.join(map(str, self.numbers))
    
# Fraction object. Represents a fraction as an integer divided by another integer. 
# The class is initiated with 'top' and 'bottom' corresponding to the numerator and 
# denominator, respectively. These are stored as class variables. The class has 
# overridden methods for string and float representation, as well as comparisons with > and <. 

class Fraction(object):
    def __init__(self, top, bottom): # Initiate fraction representation.
        self.numerator = top
        self.denominator = bottom

    def __str__(self): # return a string representation of the object
        return str(self.numerator) + "/" + str(self.denominator)

    def __float__(self): # return the fraction object as a floating point number
        return float(self.numerator/self.denominator)

    def __gt__(self, other): # return true if this fraction is greater than the other
        if(float(self) > float(other)):
            return True
        else: 
            return False

    def __lt__(self, other): # return true if this fraction is less than the other
        if(float(self) < float(other)):
            return True
        else: 
            return False

# return a list of size listSize containing random integers
def GenerateIntegerList(listSize):
    return [random.randint(0,100) for i in range(listSize)] 

# return a list of size listSize containing random Fraction objects
def GenerateFractionList(listSize):
    return [Fraction(random.randint(1,100), random.randint(1,100)) for i in range(listSize)]

# return a list of the timings for sorting a list using the 3 sorting algorithms
# Structure:
# 1. sort with algorithm
# 2. add timing to list
# 3. reset sort object list contents 
# 4. repeat 1-3 until all algorithm times recorded
# Note: Insertion sort must be first or the processor will execute the algorithm too quickly
# using cached calculations from SelectionSort
def getTimings(list):
    sort = Sort(list) # create sort object and initiate with list
    timings = [sort.numbersSize] # append the list size to the beginning of the returned list 
    sort.InsertionSort()
    timings.append(sort.elapsedTime)
    sort.elapsedTime = 0

    sort.numbers = list
    sort.SelectionSort()
    timings.append(sort.elapsedTime)
    sort.elapsedTime = 0

    sort.numbers = list
    sort.BubbleSort()
    timings.append(sort.elapsedTime)
    sort.elapsedTime = 0
    return timings # return sort timings as a list

   
# Executed function. Generate 'numberLists' number of lists of Integers and Fractions of 
# size listSize. Get the timings to sort these lists with the getTimings function. These 
# timings may be optionally written to a file as a comma seperated list. 
def main():
    # Create 20 lists of size between 2000 and 4000
    listSize = [random.randint(20,40) for i in range(20)] 
    listSize = [int for i in range(100,200,10)] 
    
    # How many times to repeat the same list size
    numberLists = 3
    IntegerTimingsList = []
    FractionsTimingsList = []
    # Generate a list of lists of integers
    for listsize in listSize:
        IntegerTimingsList.append([getTimings(list) for list in [GenerateIntegerList(listsize) 
                                                                for i in range(numberLists)]])
        # Generate a list of lists of fractions
        FractionsTimingsList.append([getTimings(list) for list in [GenerateFractionList(listsize) 
                                                                  for i in range(numberLists)]])

    avgIntegerTimingsDict = {}
    for sameSizeLists in IntegerTimingsList:
        timingsDict = {'size':0, 'insert':0, 'selection':0, 'bubble':0}
        for timingsList in sameSizeLists:
            timingsDict['size'] = timingsList[0]
            timingsDict['insert'] = timingsDict['insert'] + float(timingsList[1])
            timingsDict['selection'] += float(timingsList[2])
            timingsDict['bubble'] += float(timingsList[3])
        avgIntegerTimingsDict[timingsDict['size']] = [timingsDict['insert']/len(sameSizeLists), timingsDict['selection']/len(sameSizeLists),
                                               timingsDict['bubble']/len(sameSizeLists)]
    
    print("Integer average timings:")
    for timingsListKey in avgIntegerTimingsDict:
        print("Size:", timingsListKey, avgIntegerTimingsDict[timingsListKey])
    
    avgFractionsTimingsDict = {}
    for sameSizeLists in FractionsTimingsList:
        timingsDict = {'size':0, 'insert':0, 'selection':0, 'bubble':0}
        for timingsList in sameSizeLists:
            timingsDict['size'] = timingsList[0]
            timingsDict['insert'] = timingsDict['insert'] + float(timingsList[1])
            timingsDict['selection'] += float(timingsList[2])
            timingsDict['bubble'] += float(timingsList[3])
        avgFractionsTimingsDict[timingsDict['size']] = [timingsDict['insert']/len(sameSizeLists), timingsDict['selection']/len(sameSizeLists),
                                               timingsDict['bubble']/len(sameSizeLists)]
    print("\nFractions average timings:")
    for timingsListKey in avgFractionsTimingsDict:
        print("Size:", timingsListKey, avgIntegerTimingsDict[timingsListKey])   
 

        #Writing integer list timing contents to a text file. I commented out the actual function so new
        #files aren't created every time we run the program.
        #with open("IntegerTimings.txt", "w") as output:
            #output.write(str(list))
        #output.close()


        #Writing fraction list timing contents to a text file. I commented out the actual function so new
        #files aren't created every time we run the program.
        #with open("FractionTimings.txt", "w") as output:
            #output.write(str(list))
        #output.close()

   
main()

## referenced https://runestone.academy/runestone/books/published/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html 
## on 9/25/19 as a basis for the Fractions object structure