import random 

class Sort(object):
    numbers = []
    numbersSize = len(numbers)

    #optionally overload with an initiating list
    def __init__(self):
      pass

    def SelectionSort(self):
       i = 0
       j= 0
       indexSmallest = 0
       temp = 0   
    
       for i in range(0, self.numbersSize):
           indexSmallest = i
           for j in range(i+1, self.numbersSize):
             if  self.numbers[j] < self.numbers[indexSmallest]:
                indexSmallest = j
         
           temp = self.numbers[i]
           self.numbers[i] = self.numbers[indexSmallest]
           self.numbers[indexSmallest] = temp
  

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

    def Partition(self, numbers, i, k):
        l = 0
        h = 0
        midpoint = 0
        pivot = 0
        temp = 0
        done = false

        midpoint = i + (k - i) / 2
        pivot = numbers[midpoint]
        l = i
        h = k 

        while not done:
            while numbers[i] < pivot:
                l += 1
            while pivot < numbers[h]:
                h -= 1
            if l >= h:
                done = true
            else:
                temp = numbers[l]
                numbers[l] = numbers[h]
                numbers[h] = temp
                l += 1
                h -= 1
        return h

    def Quicksort(self, numbers, i, k):
        j = 0 

        if i >= k:
            return

        j = Partition(self.numbers, i , k)
    
        Quicksort(self.numbers, i, j)
        Quicksort(self.numbers, j + 1, k)

    def NumberInput(self):
        print("Enter numbers to sort. n to stop.")
        while(True):
            x = input("")
            if x == "n":
                break
            self.numbers.append(int(x))
        self.numbersSize = len(self.numbers)

    def PrintNums(self):
        print(self.numbers)

    def ClearList(self):
        self.numbers.clear()

    def ShuffleList(self):
        temp = random.shuffle(self.numbers)
        self.numbers = temp




def main():
  
   numSort = Sort()
   numSort.NumberInput()
   numSort.PrintNums()
   numSort.SelectionSort()
   numSort.PrintNums()
   numSort.ShuffleList()
   numSort.PrintNums()
#   numSort.BubbleSort()
   numSort.PrintNums()
   numSort.ShuffleList()
   numSort.InsertionSort()
   numSort.PrintNums()
 
     

main()
