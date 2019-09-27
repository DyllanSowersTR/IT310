## referenced https://runestone.academy/runestone/books/published/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html 
## on 9/25/19

## Questions: Do the integers and fraction objects need to be sorted in the same list?
## May need to overload the operators to compare integers and objects, not sure if this would be in Fractions or Sort

import time
import random

class Sort(object):
    numbers = []
    elapsedTime = 0

    #optionally overload with an initiating list
    def __init__(self, numList):
      self.numbers = numList
      self.numbersSize = len(self.numbers)

    def SelectionSort(self):
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


    def InsertionSort(self):
        i = 0
        j = 0
        temp = 0
        startTime = time.time()
        for i in range(1, self.numbersSize):
            j = i
            while j > 0 and numbers[j] < self.numbers[j - 1]:
                temp = numbers[j]
                self.numbers[j] = self.numbers[j - 1]
                self.numbers[j - 1] = temp 
                j -= 1
        endTime = time.time()
        self.updateTime(startTime, endTime)
 
    def BubbleSort(self):
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
       return str(self.numerator) + "/" + str(self.denominator)

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
        if(this > that):
            return True
        else: 
            return False


def GenerateIntegerList(listSize):
    return [random.randint(0,100) for i in range(random.randint(10,listSize))] 
   
def GenerateFractionList(listSize):
    return [Fraction(random.randint(1,100), random.randint(1,100)) for i in range(random.randint(10, listSize))]

def main():
    list = GenerateList() 
    sort = Sort(list)
    ## Printing the list itself will print memory locations for the objects for some reason
    print("Unsorted:")
    for item in list:
        print(item)
    sort.SelectionSort()
    print("Sorted:")
    for item in sort.getList():
        print(item)
  
    
main()