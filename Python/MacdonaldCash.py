change=int(input("How much change do you need to give back? 0."))
answerList=[]



answerList.append(int(change/25))       #This divides the input by 25 to check how many quarters go into it and then puts the amount of quarters in the list
change=change%25                        #This finds the modulo (or remainder) of the quarters

answerList.append(int(change/10))       #This divides the modulo from the quarters by 10 to check how many dimes go into it and then puts the amount of dimes in the list
change=change%10                        #This finds the modulo (or remainder) of the dimes


answerList.append(int(change/5))        #This divides the modulo from the dimes by 5 to check how many nickels go into it and then puts the amount of nickels in the list
change=change%5                         #This finds the modulo (or remainder) of the nickels


answerList.append(int(change/1))        #This divides the modulo from the nickels by 1 to check how many pennies go into it and then puts the amount of pennies in the lis
change=change%1                         #This finds the modulo (or remainder) of the pennies just to make sure I did this right and to make sure it is 0



if answerList[0]!=1:            #checks if the number of quarters from the list is more than one. If it is it will add an s to make it plural
    print(answerList[0],"quarters")
else:
    print(answerList[0], "quarter")

if answerList[1]!=1:            #checks if the number of dimes from the list is more than one. If it is it will add an s to make it plural
    print(answerList[1], "dimes")
else:
    print(answerList[1], "dime")

if answerList[2]!=1:            #checks if the number of nickels from the list is more than one. If it is it will add an s to make it plural
    print(answerList[2],"nickels")
else:
    print(answerList[2], "nickel")

if answerList[3]!=1:            #checks if the number of pennies from the list is more than one. If it is it will add an s to make it plural
    print(answerList[3], "pennies")
else:
    print(answerList[3], "penny")


