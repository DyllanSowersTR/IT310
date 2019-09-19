import random

#Got some help from StackOverflow, but created it into my own code with additional code for personal touch as well.
#https://stackoverflow.com/questions/46709794/birthday-paradox-python-incorrect-probability-output

#Definition for the birthday paradox listing
def BirthdayParadox():


    #Create empty list
    birthdayList = []
    #Insert random integers from 1 to 365 (days in the year) with a total of 25 integers or (people) 
    #I chose 25 people because it is more than 23.
    birthdayList = [random.randint(1, 365) for i in range(25)]
    #Sort the random int list from smallest to largest
    birthdayList.sort()
   
    #Create a check that runs through the list to find matches. 
    #If true, there is a match and will add to total number of matches in my pring statements further down.
    for a in range(len(birthdayList)):
        while a < (len(birthdayList))-1:
            if birthdayList [a] == birthdayList [a+1]:
                #Printed list for testing
                #print(birthdayList[a])
                return True
            a = a + 1
        return False

#Create a counter to select your total amount of times to run through the list
count = 0
rangeNum = 1000
for i in range (rangeNum):
    if BirthdayParadox() == True:
        count = count + 1

#I created 2 print statements for grammar checks since it bothered me when there was only one match
if count == 1:
    print('Out of 25 people... in', rangeNum, 'full list checks, there was', count, 'match for 2 people with the same birthdays.')
else:
    print('Out of 25 people... in', rangeNum, 'full list checks, there were', count, 'matches for 2 people with the same birthdays.')


#Call the defintion to run the code    
BirthdayParadox()