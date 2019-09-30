## referenced https://runestone.academy/runestone/books/published/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html 
## on 9/25/19


import time
import random

class Sort(object):
    numbers = []
    elapsedTime = 0

    def __init__(self, numList):
      self.numbers = numList
      self.numbersSize = len(self.numbers)

    def SelectionSort(self): # confirmed to work
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
       self.updateTime(startTime, endTime)


    def InsertionSort(self): # confirmed to work
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
        self.updateTime(startTime, endTime)
 
    def BubbleSort(self): # works, sorts in descending order though
        startTime = time.time() 

        for i in range(0, self.numbersSize - 1):
            for j in range(0, self.numbersSize - i - 1):
                if self.numbers[j] > self.numbers[j + 1]:
                    temp = self.numbers[j]
                    self.numbers[j] = self.numbers[j + 1]
                    self.numbers[j + 1] = temp
        endTime = time.time()
        self.updateTime(startTime, endTime)

    def updateTime(self, startTime, endTime):
        self.elapsedTime = endTime - startTime

    def getList(self):
        return self.numbers
    
   
    
class Fraction(object):
    def __init__(self, top, bottom):
        self.numerator = top
        self.denominator = bottom

    def __str__(self):
      # return str(self.numerator) + "/" + str(self.denominator)
       return str(float(self.numerator/self.denominator))

    def asDecimal(self):
        return float(self.numerator/self.denominator)

    def __gt__(self, other):
        this = self.asDecimal()
        if other is Fraction:
            that = other.asDecimal()
        else:
            that = other

        if(this > that):
            return True
        else: 
            return False

    def __lt__(self, other):
        this = self.asDecimal()
        if other is Fraction:
            that = other.asDecimal()
        else:
            that = other
        if(this < that):
            return True
        else: 
            return False


def GenerateIntegerList(listSize):
    return [random.randint(0,100) for i in range(listSize)] 
   
def GenerateFractionList(listSize):
    return [Fraction(random.randint(1,100), random.randint(1,100)) for i in range(listSize)]

def getTimings(list):
    sort = Sort(list)

    sort.SelectionSort()
    timings = [sort.elapsedTime]
    sort.elapsedTime = 0

    sort.numbers = list
    sort.InsertionSort()
    timings.append(sort.elapsedTime)
    sort.elapsedTime = 0

    sort.numbers = list
    sort.BubbleSort()
    timings.append(sort.elapsedTime)
    sort.elapsedTime = 0
    return timings

   

def main():
    listSize = 500
    numberLists = 10
    IntegerTimingsList = [getTimings(list) for list in [GenerateIntegerList(listSize) for i in range(numberLists)]]
    FractionsTimingsList = [getTimings(list) for list in [GenerateFractionList(listSize) for i in range(numberLists)]]
    print("Integer timings: ")
    for list in IntegerTimingsList:
        print(list)
    print("Fractions timings")
    for list in FractionsTimingsList:
        print(list)
   
    


      
main()
