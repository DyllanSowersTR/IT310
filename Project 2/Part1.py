## referenced https://runestone.academy/runestone/books/published/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html 
## on 9/25/19

import time

class Sort(object):
    numbers = []
    elapsedTime = 0

    #optionally overload with an initiating list
    def __init__(self, numList):
      self.numbers = numList
      self.numberSize = len(self.numbers)

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
       updateTime(startTime, endTime)


    def InsertionSort(self):
        i = 0
        j = 0
        temp = 0

        for i in range(1, self.numbersSize):
            j = i
            while j > 0 and numbers[j] < self.numbers[j - 1]:
                temp = numbers[j]
                self.numbers[j] = self.numbers[j - 1]
                self.numbers[j - 1] = temp 
                j -= 1

    def BubbleSort(self):
        for i in range(0, self.numbersSize - 1):
            for j in range(0, self.numbersSize - i - 1):
                if self.numbers[j] > self.numbers[j + 1]:
                    temp = self.numbers[j]
                    self.numbers[j] = self.numbers[j + 1]
                    self.numbers[j + 1] = temp

    def updateTime(self, startTime, endTime):
        self.elapsedTime = endTime - startTime

class Fraction(object):
    def __init__(self, top, bottom):
        self.numerator = top
        self.denominator = bottom
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    def asDecimal(self):
        return float(numerator/denominator)
    