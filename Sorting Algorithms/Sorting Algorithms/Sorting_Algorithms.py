def SelectionSort(numbers, numbersSize):
   i = 0
   j = 0
   indexSmallest = 0
   temp = 0   
   
   for i in range(0, numbersSize):
       indexSmallest = i
       for j in range(i+1, numbersSize):
         if  numbers[j] < numbers[indexSmallest]:
            indexSmallest = j
         
       temp = numbers[i]
       numbers[i] = numbers[indexSmallest]
       numbers[indexSmallest] = temp
   


def main():
   numbers = [ 5, 86, 69, 73, 11, 17, 1, 74, 34, 3 ]
   NUMBERS_SIZE = 8
   i = 0
   
   print("UNSORTED: ")
   for i in range(0, NUMBERS_SIZE):
      print(str(numbers[i]) + " ")
   
   print("\n")
   SelectionSort(numbers, NUMBERS_SIZE)
   
   print("SORTED: ")
   for i in range(0, NUMBERS_SIZE):
      print(str(numbers[i]) + " ")
     

main()
