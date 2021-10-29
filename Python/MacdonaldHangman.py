import random 
print("Welcome to hangman! ")
wordList=["elephant","tigers","lasagna"]
word= random.choice(wordList)   #this choses a random word from the list above
strikes=0
lines=[]





point1="""
 ---------
 |       |
()       |
         |
         |
         |
----------------
"""

point2="""
---------
 |       |
()       |
 |       |
 |       |
         |
----------------
"""

point3="""
---------
  |      |
 ()      |
 \|      |
  |      |
         |
----------------
"""

point4="""
---------
  |      |
 ()      |
 \|/     |
  |      |
         |
----------------
"""

point5="""
---------
  |      |
 ()      |
 \|/     |
  |      |
 /       |
----------------
"""
point6="""
---------
  |      |
 ()      |
 \|/     |
  |      |
 / \      |
----------------
"""




print("strikes =",strikes) 

for i in range(len(word)):  #this will print the same amount of spaces for how many letters are in the word
    lines.append("_")       #this will append the spaces into a list

print(str(' '.join(lines)))     #this will print out the spaces neatly




userInput=input("\nEnter a letter...But be careful, 6 strikes and you lose... ").lower()
while (not userInput.isalpha()):
    userInput=input("\nEnter a letter...But be careful, 6 strikes and you lose... ").lower()


while userInput!="|":           #this just helps iterate through the loop
    if userInput not in word:           #if the letter the user picked isn't in the word then it will add 1 to the strikes count
        strikes+=1
        if strikes==1:      #these will print the hangman art according to how many strikes the user has
            print(point1)
        elif strikes==2:
            print(point2)
        elif strikes==3:
            print(point3)
        elif strikes==4:
            print(point4)
        elif strikes==5:
            print(point5)
        
        
        if strikes==6:      #If the strikes =6 then it will stop the game and say game over
            print("Game over the word was...",word)
            print(point6)
            break
        else:       #if it's not =6 then it will print out the strikes the word with lines and another input
            print("strikes =",strikes)
            print(str(' '.join(lines)))
            userInput=input("\nEnter a letter...But be careful, 6 strikes and you lose... ").lower()
            while (not userInput.isalpha()):
                userInput=input("\nEnter a letter...But be careful, 6 strikes and you lose... ").lower()

    if userInput in word:
        for i in range(len(word)):      #if the letter is in the word it will find that index that letter is in in the word and take the same index of the lines and replace it with the letter
            if word[i]==userInput:
                lines[i]=userInput
        if "_" not in lines:        #if there isn't any spaces in the lines then it means the user guessed the word correctly and it will print you won and stop the game
            print("You won!")
            print(str(' '.join(lines)))
            break 
        else:               #if there is still a space in lines then it will print the strikes, the word with lines, and another input
            print("strikes =",strikes)
            print(str(' '.join(lines)))
            userInput=input("\nEnter a letter...But be careful, 6 strikes and you lose... ").lower()
            while (not userInput.isalpha()):
                userInput=input("\nEnter a letter...But be careful, 6 strikes and you lose... ").lower()







    
    

