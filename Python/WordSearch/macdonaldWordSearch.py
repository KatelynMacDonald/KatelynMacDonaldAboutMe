wordSearch=""
puzzleList=[]
puzzle=""
def printFile(fileName):   

    #this prints out the puzzle without the tabs
    global puzzleList,wordSearch,puzzle
    file = open(fileName,"r")
    for line in file:
        puzzle=line.split()         #this takes the tabs away           https://www.kite.com/python/answers/how-to-remove-spaces,-tabs,-and-newlines-in-a-string-in-python
        puzzleList.append(puzzle)
        print(puzzle)
        wordSearch+=(" ".join(puzzle))     #this will join the letters again
        wordSearch+="\n"
        #print(wordSearch)
    file.close()

"""def printPuzzle(printPuzzle):                       #WHEN IT FINDS THE WORD AND I GO BACK AND TRY TO CHANGE IT TO A BLANK STRING JUST APPEND THE I AND R TO A LIST OR PRINT IT AND THEN BREAK INSTEAD OF TRYING TO DELETE THE WORD
    global wordSearch,puzzle
    wordSearch=""
    for i in range(len(printPuzzle)):
        for r in range(len(printPuzzle[i])):
            puzzle+=printPuzzle[i][r]
            wordSearch+=(" ".join(puzzle))     #this will join the letters again
            #print(wordSearch)
            puzzle=""
        wordSearch+="\n"
    print(wordSearch)"""



def checkforhorz(puzzleList):
    
    line=""
    for i in range(len(puzzleList)):
        for r in range(len(puzzleList[i])):
            line+=str(puzzleList[i][r])             #this puts the letter into a string to be able to check it
        #print(line)
        if uiWord in line:                      #if the user input is in the line it will print that it found it and break
            print("found it-check horz")
            #print(f"row{i} column{r}")
            for b in range(len(puzzleList[i])):                 #this will go back through the list and if the first letter of the word matches and the next one matches the next letter in the word  then it will print the index of the first letter
                #print(i,b)
                if uiWord[0]== puzzleList[i][b] and uiWord[1]==puzzleList[i][b+1]:
                    #print("Yes")
                    print("The beginning of the word starts at: ",i,b)
                    #printPuzzle.append(" ")
                    break
            break
            
        else:                                   #if it doesn't then it will reset the line and print no
            line=""
            #printPuzzle.append(puzzleList[i][r])
            #print("no")
    
def checkbackhorz(puzzleList):
    line=""
    for i in range(len(puzzleList)):
        for r in range(len(puzzleList[i])):
            line+=str(puzzleList[i][r])             #this puts the letter into a string to be able to check it
        newLine = line[::-1]                      #this reverses the string                            #https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
        print(newLine)
        if uiWord in newLine:                   #if the user input is in the line it will print that it found it and break
            print("found it-check back horz")
            for b in range(len(puzzleList[i])):                 #this will go back through the list and if the first letter of the word matches and the next one matches the next letter in the word  then it will print the index of the first letter
                #print(uiWord[-1])
                if uiWord[0]== puzzleList[i][b] and uiWord[1]==puzzleList[i][b-1]:
                    #print("Yes")
                    print("The beginning of the word starts at: ",i,b)
                    #printPuzzle.append(" ")
                    break
            break
        else:                                   #if it doesn't then it will reset the line and print no
            line=""
            #print("no")


def checkdown(puzzleList):
    #length=len(puzzleList[1])
    #print(length)
    iteration=0                                     #the variable is to make sure it grabs the same item in the list every time until it goes to a new line
    line=""
    for l in range(len(puzzleList[1])):                     #this will do it for the length of how many letters are in the first string because they should all be the same length
        for i in range(len(puzzleList)):
            #for r in range(len(puzzleList[i])):                 
                line+=str(puzzleList[i][iteration])                 #this puts the letter into a string to be able to check it
                #break
        #print(line)
        if uiWord in line:                                  #if the user input is in the line it will print that it found it and break
            print("found it-check down")
            print(f"in column: {l}")
            print(f"in row: {line.index(uiWord)}")
            break
        else:                                   #if it doesn't then it will reset the line and add 1 to the iteration so it looks for the next line down
            line=""
            #print("no")
            iteration+=1

def checkup(puzzleList):
    #print(length)
    iteration=0                                     #the variable is to make sure it grabs the same item in the list every time until it goes to a new line
    line=""
    for l in range(len(puzzleList[1])):                          #this will do it for the length of how many letters are in the first string because they should all be the same length
        for i in range(len(puzzleList)):
            #for r in range(len(puzzleList[i])):
                line+=str(puzzleList[i][iteration])                     #this puts the letter into a string to be able to check it
                #print(puzzleList[i])
                #break
        #print(puzzleList[r])
        newLine = line[::-1]                            #this reverses the string 
        #print(newLine)
        if uiWord in newLine:                       #if the user input is in the line it will print that it found it and break
            print("found it-check up")
            print(f"in column: {l}")
            print(f"in row: {line.index(uiWord[0])}")
            break
        else:                                       #if it doesn't then it will reset the line and print no and add 1 to the iteration so it looks for the next line down
            line=""
            #print("no")
            iteration+=1


def diadown(puzzleList):
    out=""
    diagonalboard=[]
    #diagonal bottom half
    for r in range(len(puzzleList)):                    #this will get the bottom half of the board
        for c in range(len(puzzleList[0])):
            #print(str(r)+str(c),end=" ")
            #print(puzzleList[r][c],end=" ")
            out+=puzzleList[r][c]                   #this will put all the letters together in one string to see if the word is in it
            if uiWord in out:
                    print("found it")                               #if it found the word it will print where it is and reset to the next line
                    print(f"in column: {c-(len(uiWord)-1)}")            
                    print(f"in row: {out.index(uiWord)}")               
                    out=""                          
                    break   
            r+=1
            c+=1
            if r>=(len(puzzleList)) or (c>=(len(puzzleList[0]))):           #if we are at the end of the board then it will reset and go to the next one
                #print(out)
                
                diagonalboard.append(out)
                out=""
                break
        #print()
        #break
    #print("\n"*3)
    for c in range(len(puzzleList[0])):                 #this will get the top half of the board
        for r in range(len(puzzleList)):
            #print(str(r)+str(c),end=" ")
            #print(puzzleList[r][c],end=" ")
            out+=puzzleList[r][c]                       #this will put all the letters together in one string to see if the word is in it
            #print(r,c)
            if uiWord in out:
                    print("found it")                               #if it found the word it will print where it is and reset to the next line
                    #print(r-(len(uiWord)-1),c-(len(uiWord)-1))
                    print(f"in column: {c-(len(uiWord)-1)} ")
                    print(f"in row: {out.index(uiWord)} ")
                    out=""
                    break
                   
            r+=1
            c+=1
            
            if r>=(len(puzzleList)) or (c>=(len(puzzleList[0]))):               #if we are at the end of the board then it will reset and go to the next one
                
                diagonalboard.append(out)
                out=""
                break
        #print()
        #break
    #print("\n"*3)
    #print(diagonalboard)
    #print(puzzleList)


def diadownback(puzzleList):
    out=""
    diagonalboard=[]
    #diagonal bottom half
    for r in range(len(puzzleList)):                    
        for c in range(len(puzzleList[::-1])):
            #print(str(r)+str(c),end=" ")
            print(puzzleList[r][c],end=" ")
            out+=puzzleList[r][c]
            r-=1
            c-=1
            if r>=(len(puzzleList)) or (c>=(len(puzzleList[0]))):               #USE A WHILE LOOP AT THE TOP INSTEAD OF A FOR AND USE THE STUFF IN HERE
                print(out)
                if uiWord in out:
                    print("found it")
                diagonalboard.append(out)
                out=""
                break
        print()
        #break
    print("\n"*3)
    for c in range(len(puzzleList[::-1])):
        for r in range(len(puzzleList)):
            #print(str(r)+str(c),end=" ")
            print(puzzleList[r][c],end=" ")
            out+=puzzleList[r][c]
            r-=1
            c-=1
            if r>=(len(puzzleList)) or (c>=(len(puzzleList[0]))):
                if uiWord in out:
                    print("found it")
                for b in range(len(puzzleList[i])):
                    l=0
                    if uiWord[l]== puzzleList[i][b]:
                        #print("Yes")
                        puzzleList[i][b]=" "
                        l+=1
                    if l>= len(uiWord):
                        break
                diagonalboard.append(out)
                out=""
                break
        print()
        #break
    print("\n"*3)
    #print(diagonalboard)
    print(puzzleList)

    



printFile("wordSearchTest.txt")



for i in range(len(puzzleList)):
    if (len(puzzleList[i])%2) != (len(puzzleList)%2):       #This makes sure that the width matches the length
        print("\n This contains bad data \n Cannot use this word search \n Please check your board\n")
        break
    else:
        print (wordSearch)              #if it matches it will print out the word search




uiWord= input("Please enter the word that you want to be found ").upper()


checkforhorz(puzzleList)

checkbackhorz(puzzleList)

checkdown(puzzleList)

checkup(puzzleList)

diadown(puzzleList)


#print(puzzleList)

#diadownback(puzzleList)
#print (wordSearch) 
#print("Print puzzle", printPuzzle)
#for the same line go throught the list and see if the word is in it and to go backwards use the .reverse method and look
        




"""
What bander showed us

word= "italian".upper()
wordReverse=word[::-1]
row= "G\tI\tT\tA\tL\tI\tA\tN\tD\tJ"
row=row.replace("\t),""
print(row)
if word in row or wordReverse in row:
    print("in row #)



def creatBoard():
    filename="WordSearchTest.txt"
    file=open(filename,"r")
    board=[]
    row=[]

    for line in file:
        #rstrip to remove the \n and split the line on the \t
        row=line.rstrip().split("\t)
        board.append(row)

    print(board)



#print board like it is in the file(horizontal)
    for r in range(len(Board)):
        for c in range(len(board[0])):
            print(board[r][c],end="")
        print()

#rotate the board 90 degrees(verical)
    for c in range(len(board[0])):
        for r in range(len(Board)):
            print(board[r][c],end="")
        print()
    


#diagonal
    for r in range(len(Board)):
        for c in range(len(board[0])):
            print(str(r)+str(c),end=" ")
            r+=1
            c+=1
        #print()
        break
print("\n"*3)

"""


