import random 
from Reset import Reset


totalPlayer1Score=0
totalPlayer2Score=0



def printBoard(b):          #this will print the board out like tic tac toe 
    for row in range(len(b)):
        for col in range(len(b[row])):
            if col != (len(b[row])-1):
                print(b[row][col], end=" | ")
            else:
                print(b[row][col], end="\n")
        if row != (len(b)-1):
            print("-"*25)
    print()



def addMark(m,r,c,b):
    #if the space is blamk add the mark and tell the program we are good
    if b[r][c]==" ":
        b[r][c]=m
        return True
    return False



#catGame        return true if we do have a cat game
def catChecker(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c]==" ":
                return False
    print("Cat game")
    return True

def rowChecker(b):
    for r in range(len(b)):
        for c in range(len(b[r])-3):        #the -3 is there so it doesn't error when you add to it below
            #to make this more dynamic, I need to iterate through each item in the row
            if  b[r][c]!=" " and b[r][c]==b[r][c+1] and b[r][c+1]==b[r][c+2] and b[r][c+2]==b[r][c+3]:
                    print("RowChecker Spotted a winner!")
                    return (True)
    return False

def colChecker(b):      #this will check the columns to see if there is a winner
    for r in range(len(b)):
        for c in range(len(b[r])):
            if b[r][c]!=" " and b[r][c]==b[r-1][c] and b[r-1][c]==b[r-2][c] and b[r-2][c]==b[r-3][c]:
                    print("Col checker spotted a winner")
                    return (True)
    return False


def diaChecker(b):
    for r in range(len(b)):             #can't put these 2 together because of having to have the -3 for one. You can't have the -3 on both of them
        for c in range(len(b[r])-3):        #this is to go from bottom left to top right
            if b[r][c]!=" " and b[r][c]==b[r-1][c+1] and b[r-1][c+1]==b[r-2][c+2] and b[r-2][c+2]==b[r-3][c+3]:
                    print("dia checker spotted a winner")
                    return (True)
    for r in range(len(b)):             #this is to go from bottom right to top left
        for c in range(len(b[r])):
            if b[r][c]!=" " and b[r][c]==b[r-1][c-1] and b[r-1][c-1]==b[r-2][c-2] and b[r-2][c-2]==b[r-3][c-3]:
                    print("dia checker spotted a winner")
                    return (True)
    return False

def checkForWinner(b):
    checkForWinnerList=[(rowChecker(b)) , (colChecker(b)) , (diaChecker(b))]
    #if rowChecker(b) or colChecker(b) or diaChecker(b):                #more efficient for time
    if True in checkForWinnerList:         #is a checklist
        return True
    return False   


row,col=0,0


markList=["X","O"]
player1Mark=input("What would you like to be... X or O? ").upper()   #this asks the user what they would like to be
player1Mark=Reset(player1Mark)      #this is the class to make sure that the user inputs x or o
markList.remove(player1Mark.player1Mark)     #whatever they pick it will remove it from the list and make the computer the remaining mark
player2Mark=markList[0]
print("Player 1 Mark:",player1Mark)
print("Player 2 Mark:",player2Mark)
mark=player1Mark
print(type(mark))
board=[[" "," "," "," "," "," "," "],[" "," "," "," "," "," ", " "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," ", " "],[" "," "," "," "," "," ", " "],[" "," "," "," "," "," ", " "]]




print("""


   ____   U  ___ u  _   _     _   _   U _____ u   ____  _____       _  _    
U /"___|   \/"_ \/ | \ |"|   | \ |"|  \| ___"|/U /"___||_ " _|     | ||"|   
\| | u     | | | |<|  \| |> <|  \| |>  |  _|"  \| | u    | |       | || |_  
 | |/__.-,_| |_| |U| |\  |u U| |\  |u  | |___   | |/__  /| |\      |__   _| 
  \____|\_)-\___/  |_| \_|   |_| \_|   |_____|   \____|u |_|U        /|_|\  
 _// \\\\      \\\\    ||   \\\\,-.||   \\\\,-.<<   >>  _// \\\\ _// \\\\_      u_|||_u 
(__)(__)    (__)   (_")  (_/ (_")  (_/(__) (__)(__)(__|__) (__)     (__)__) 

""")
ui=input("Type anything to continue...If you are done playing type done ").lower()
printBoard(board)
while ui!="done":
    while mark!="q":
        correctInput=False
        row=5
        while not correctInput:
            print()
            col=int(input("Which col? "))-1
            print()
            columnFull=[]
            
                #print(columnFull)
            #check to see if the ui is in the actual board
            if not (0<=col<=6):
                print("The column is not correct")
                    
        
            else:       
                 #goes through the column that the user wants and makes sure it isn't full
                for i in range( len(board)):
                    columnFull.append(board[i][col])
                #if the column is full it will not let the user put their marker there
                if " " not in columnFull:
                    print("That column is full")
                else:
                    #this will add the mark to the board and make it go to the bottom
                    while not(addMark(mark, row, col, board)):
                        row-=1
                    correctInput=True           #this breaks the loop

        

        """
            after checking for input do the following:
                print your board to the user
                check to see if we have a game over
                    if we do have a gameOver, mark="q"
                    if we do not have a gameOver, mark ="O"
        """



        printBoard(board)
        #if we have a gameOver set mark to q and be done with it
        if(checkForWinner(board)):          #these will check to see if the winner was the player1 or the player2 and then will add 1 to their score
            if rowChecker(board)==True:
                    if  mark==player1Mark:
                        totalPlayer1Score+=1
                    else:
                        totalPlayer2Score+=1
            elif colChecker(board)==True:
                if mark==player1Mark:
                    totalPlayer1Score+=1
                else:
                    totalPlayer2Score+=1
            elif diaChecker(board)==True:
                if mark==player1Mark:
                    totalPlayer1Score+=1
                else:
                    totalPlayer2Score+=1
            print("Player 1 Score",totalPlayer1Score)
            print("Player 2 Score", totalPlayer2Score)
            mark="q" 
            
        elif(catChecker(board)):
            print("Player 1 Score",totalPlayer1Score)
            print("Player 2 Score", totalPlayer2Score)
            mark="q" 
        #if no game over, then change mark
        elif mark==player1Mark:
            mark=player2Mark
        #if mark was O and no gameOver, change mark
        else:
            mark=player1Mark
    ui=input("Would you like to play again? If not type 'done' ").lower()       #if they don't type done then the game will reset and they can play again
    if ui=="done":      #if the user types in done then the game will stop
        break


    #this will reset the game if they want to play again
    row,col=0,0
    markList=["X","O"]
    player1Mark=input("What would you like to be... X or O? ").upper()   #this asks the user what they would like to be
    player1Mark=Reset(player1Mark)  #this is the class to make sure that the user inputs x or o
    markList.remove(player1Mark.player1Mark)     #whatever they pick it will remove it from the list and make the computer the remaining mark
    player2Mark=markList[0]
    print("Player 1 Mark:",player1Mark)
    print("Player 2 Mark:",player2Mark)
    mark=player1Mark
    board=[[" "," "," "," "," "," "," "],[" "," "," "," "," "," ", " "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," ", " "],[" "," "," "," "," "," ", " "],[" "," "," "," "," "," ", " "]]
    printBoard(board)





