#snake2.0

#Items I put in
"""
PVP(+5) - line 305
Snake speeds up as you eat(+5) - line 250 in normal 341 and 408 in pvp
Pause button(+5) - line 211
Window has a title(+1) - line 50
Main Menu(+5) - line 111 and 183
Directions in console(+1) - line 228 in normal 318 in pvp
Directions in window(+3) - line 238 in normal 329 in pvp
Change color after ate food(+3)- line 252 in normal 343 in pvp

"""



#imports
import turtle as t 
import random 
import time 





#game configuration
delay = 0.1
sizeOfHead=1
score=0
player2Score=0
bodyPartsList=[]
bodyPartsList2=[]
fontSettings=("Comic Sans MS",16,"normal")
movementAmount=20
oldMovementAmount=0
speed=1.3
speed2=1.3
colorList=["green","DarkOliveGreen1","chartreuse2","DarkGreen","DarkSeaGreen2"]
colorList2=["cyan","darkBlue","CadetBlue","aquamarine","DarkSlateGray3"]
color="green"
color2="blue"

#object creation

#window
wn = t.Screen()
wn.setup(width=600,height=600)
#gives the window a title                           https://www.geeksforgeeks.org/turtle-title-function-in-python/#:~:text=turtle.-,title(),title%20of%20the%20turtle%20window.
t.title("Snake")

#snake head
head = t.Turtle()
head.hideturtle()
head.shape("square")
head.color(color)
head.shapesize(sizeOfHead)
head.direction="stop"
head.penup()
head.speed(speed)

head2 = t.Turtle()
head2.hideturtle()
head2.shape("square")
head2.color(color2)
head2.shapesize(sizeOfHead)
head2.direction="stop"
head2.penup()
head2.speed(speed)

#snake food
food=t.Turtle()
food.hideturtle()
food.shape("turtle")
food.color("saddle brown")
food.penup()
food.goto(100,100)


#scorekeeper
scoreKeeper = t.Turtle()
scoreKeeper.hideturtle()
scoreKeeper.speed(0)
scoreKeeper.penup()



#scorekeeper for player 2
scoreKeeper2 = t.Turtle()
scoreKeeper2.hideturtle()
scoreKeeper2.speed(0)
scoreKeeper2.penup()
scoreKeeper2.goto(270,270)



#this prints out the directions
directions= t .Turtle()
directions.hideturtle()
directions.speed(0)
directions.penup()



#menu
menu= t.Turtle()
menu.hideturtle()
menu.speed(0)
menu.penup()
menu.goto(-250,100)
menu.write("Press the key for the game you want:\n\t'N' for Normal  'V' for PVP",align="left",font=fontSettings)

winner=t .Turtle()
winner.hideturtle()
winner.speed(0)
winner.penup()
winner.goto(0,0)

#function and command development

def up():
    #if head is going down, we can't go up
    if head.direction!="down":
        head.direction = "up"
def down():
    if head.direction!="up": 
        head.direction = "down"
def left():
    if head.direction!="right":
        head.direction = "left"
def right():
    if head.direction!="left":
        head.direction = "right"
def up2():
    if head2.direction!="down":
        head2.direction = "up"
def down2():
    if head2.direction!="up": 
        head2.direction = "down"
def left2():
    if head2.direction!="right":
        head2.direction = "left"
def right2():
    if head2.direction!="left":
        head2.direction = "right"

def move():
    global movementAmount
    if head.direction == "up":
        head.sety(head.ycor()+movementAmount)
    elif head.direction == "down":
        head.sety(head.ycor()-movementAmount)
    elif head.direction == "left":
        head.setx(head.xcor()-movementAmount)
    elif head.direction == "right":
        head.setx(head.xcor()+movementAmount)
    elif head.direction =="stop":
        head.goto(head.xcor(),head.ycor())
    else:
        head.goto(0,0) 
def move2():
    global movementAmount 
    if head2.direction == "up":
        head2.sety(head2.ycor()+movementAmount)
    elif head2.direction == "down":
        head2.sety(head2.ycor()-movementAmount)
    elif head2.direction == "left":
        head2.setx(head2.xcor()-movementAmount)
    elif head2.direction == "right":
        head2.setx(head2.xcor()+movementAmount)
    elif head2.direction =="stop":
        head2.goto(head2.xcor(),head2.ycor())
    else:
        head2.goto(0,0)

def die():
    global score,speed,color,speed2,color2
    directions.clear()
    head.hideturtle()
    head2.hideturtle()
    food.hideturtle()
    menu.clear()
    menu.write("Press the key for the game you want:\n\t'N' for Normal  'V' for PVP",align="left",font=fontSettings)
    time.sleep(1)
    head.goto(0,0)
    head.direction="stop"
    head2.direction="stop"
    score=0
    score2=0
    scoreKeeper.clear()
    scoreKeeper2.clear()
    head.color(color)
    head2.color(color2)
    
    for bp in bodyPartsList:
        bp.speed(0)
        bp.hideturtle()
        bp.goto(1000,1000)
    for bp in bodyPartsList2:
        bp.speed(0)
        bp.hideturtle()
        bp.goto(1000,1000)
    bodyPartsList.clear()
    bodyPartsList2.clear()
    speed=1.3
    speed2=1.3
    head.speed(speed)
    head2.speed(speed2)

#makes a pause button
def pause():
    global movementAmount, oldMovementAmount

    head.direction="stop"
    

def normal():
    #game play 
    global speed, score,delay, sizeOfHead,bodyPartsList,fontSettings,movementAmount,oldMovementAmount,speed,colorList,color
    menu.clear()
    winner.clear()
    head.showturtle()
    food.showturtle()
    scoreKeeper.goto(270,270)
    scoreKeeper.write("Score: 0", align="right",font=fontSettings)
    
    #prints out directions in console
    print("""
    up = w
    down = s
    right = d
    left = a
    pause = p
        to play the game after you have paused it press any of the direction keys
    """)
    directions.goto(-270,210)
    #this prints out the directions on the screen
    directions.write("up = w, down = s, right = d, left = a, pause = p\n -to play the game after you have paused\n it press any of the direction keys",align="left",font=fontSettings)

    while True:
        wn.update()
        if head.direction!="stop":
            #check for boundary collision
            if head.xcor()> (300-sizeOfHead/2) or head.xcor()<(-300+sizeOfHead/2) or head.ycor()> (300-sizeOfHead/2) or head.ycor()<(-300+sizeOfHead/2):       
                die()

            #object.distance(object2)
            if head.distance(food)<20:
                #movementAmount+=5
                speed+=1            #this increases the speed everytime the snake eates food
                score+=1
                newColor=random.choice(colorList)
                head.color(newColor)
                for index in range(len(bodyPartsList)-1,0,-1):
                    bodyPartsList[index].color(newColor)
                scoreKeeper.clear()
                scoreKeeper.write(("Score: "+ str(score)),align="right",font=fontSettings)

                #print("Score: {}".format(score))
                x,y=random.randint(-280,280),random.randint(-280,280)
                food.goto(x,y)

                newBodyPart = t.Turtle()
                newBodyPart.shape("square")
                newBodyPart.color(newColor)
                newBodyPart.penup()
                newBodyPart.shapesize(1)
                newBodyPart.speed(speed)
                newBodyPart.goto(score+10,0)


                bodyPartsList.append(newBodyPart)

            move()
            
                
            #moving the body parts
            #iterate through the list
            for index in range(len(bodyPartsList)-1,0,-1):
                #grabe the x,y coord of the turtle
                #print("moving the body")
                x=bodyPartsList[index-1].xcor()
                y=bodyPartsList[index-1].ycor()
                #reset the x,y coord of the next turtle
                bodyPartsList[index].goto(x,y)
                #check to see if we ate any of the body parts
                if head.distance(bodyPartsList[index])<1:
                    die()
                    break
            

            #move the neck or bodyPart[0] to where the head is
        
            if len(bodyPartsList)>0:
                bodyPartsList[0].color(newColor)
                #print("moving the neck")
                bodyPartsList[0].goto(head.xcor(),head.ycor())

            
                


            time.sleep(delay)

def PVP():
    global speed, score,delay, sizeOfHead,bodyPartsList,fontSettings,movementAmount,oldMovementAmount,colorList,color,player2Score,bodyPartsList2,speed2,color2
    winner.clear()
    menu.clear()
    head.goto(-100,0)
    head2.goto(100,0)
    head.showturtle()
    head2.showturtle()
    food.showturtle()
    scoreKeeper.goto(-250,270)
    scoreKeeper2.write("Player2: 0", align="right",font=fontSettings)
    scoreKeeper.write("Player1: 0", align="left",font=fontSettings)
    #prints out directions in console
    print("""
    Player 1:               Player 2:
    up = 'w'                up = 'up'
    down = 's'              down = 'down'
    right = 'd'             right = 'right'
    left = 'a'              left = 'left'
    pause = 'p'
        to play the game after you have paused it press any of the direction keys
    """)
    #this prints out the directions on the screen
    directions.goto(-270,120)
    directions.write("Player 1 Directions:\t\t Player 2 Directions:\nup = 'w', down = 's',\t\t up='up' down ='down'\nright = 'd', left = 'a',\t\t right ='right' left= 'left' \npause = 'p' -to play the game after you have paused\n it press any of the direction keys",align="left",font=fontSettings)

    while True:
        wn.update()
        if head.direction!="stop":
            #check for boundary collision
            if head.xcor()> (300-sizeOfHead/2) or head.xcor()<(-300+sizeOfHead/2) or head.ycor()> (300-sizeOfHead/2) or head.ycor()<(-300+sizeOfHead/2):       
                winner.write("Player 2 wins",align="center",font=fontSettings)
                die()

            #object.distance(object2)
            if head.distance(food)<20:
                speed+=1            #this increases the speed everytime the snake eates food
                score+=1
                newColor=random.choice(colorList)
                head.color(newColor)
                for index in range(len(bodyPartsList)-1,0,-1):
                    bodyPartsList[index].color(newColor)
                scoreKeeper.clear()
                scoreKeeper.write(("Player1: "+ str(score)),align="left",font=fontSettings)

                #print("Score: {}".format(score))
                x,y=random.randint(-280,280),random.randint(-280,280)
                food.goto(x,y)

                newBodyPart = t.Turtle()
                newBodyPart.shape("square")
                newBodyPart.color(newColor)
                newBodyPart.penup()
                newBodyPart.shapesize(1)
                newBodyPart.speed(speed)
                newBodyPart.goto(score+10,0)


                bodyPartsList.append(newBodyPart)

            move()
            
                
            #moving the body parts
            #iterate through the list
            for index in range(len(bodyPartsList)-1,0,-1):
                #grabe the x,y coord of the turtle
                #print("moving the body")
                x=bodyPartsList[index-1].xcor()
                y=bodyPartsList[index-1].ycor()
                #reset the x,y coord of the next turtle
                bodyPartsList[index].goto(x,y)
                #check to see if we ate any of the body parts
                if head.distance(bodyPartsList[index])<1:
                    winner.write("Player 2 wins",align="center",font=fontSettings)
                    die()
                    break
                if head2.distance(bodyPartsList[index])<1:
                    winner.write("Player 1 wins",align="center",font=fontSettings)
                    die()
                    break
            

            #move the neck or bodyPart[0] to where the head is
        
            if len(bodyPartsList)>0:
                bodyPartsList[0].color(newColor)
                #print("moving the neck")
                bodyPartsList[0].goto(head.xcor(),head.ycor())

            
                


            time.sleep(delay)
        if head2.direction!="stop":
            #check for boundary collision
            if head2.xcor()> (300-sizeOfHead/2) or head2.xcor()<(-300+sizeOfHead/2) or head2.ycor()> (300-sizeOfHead/2) or head2.ycor()<(-300+sizeOfHead/2):       
                winner.write("Player 1 Wins",align="center",font=fontSettings)
                die()

            #object.distance(object2)
            if head2.distance(food)<20:
                speed2+=1            #this increases the speed everytime the snake eates food
                player2Score+=1
                newColor2=random.choice(colorList2)
                head2.color(newColor2)
                for index in range(len(bodyPartsList2)-1,0,-1):
                    bodyPartsList2[index].color(newColor2)
                scoreKeeper2.clear()
                scoreKeeper2.write(("Player2: "+ str(player2Score)),align="right",font=fontSettings)

                #print("Score: {}".format(score))
                x,y=random.randint(-280,280),random.randint(-280,280)
                food.goto(x,y)

                newBodyPart2 = t.Turtle()
                newBodyPart2.shape("square")
                newBodyPart2.color(newColor2)
                newBodyPart2.penup()
                newBodyPart2.shapesize(1)
                newBodyPart2.speed(speed2)
                newBodyPart2.goto(score+10,0)


                bodyPartsList2.append(newBodyPart2)

            move2()
            
                
            #moving the body parts
            #iterate through the list
            for index in range(len(bodyPartsList2)-1,0,-1):
                #grabe the x,y coord of the turtle
                #print("moving the body")
                x=bodyPartsList2[index-1].xcor()
                y=bodyPartsList2[index-1].ycor()
                #reset the x,y coord of the next turtle
                bodyPartsList2[index].goto(x,y)
                #check to see if we ate any of the body parts
                if head2.distance(bodyPartsList2[index])<1:
                    winner.write("Player 1 Wins",align="center",font=fontSettings)
                    die()
                    break
                if head.distance(bodyPartsList2[index])<1:
                    winner.write("Player 2 Wins",align="center",font=fontSettings)
                    die()
                    break
            
            

            #move the neck or bodyPart[0] to where the head is
        
            if len(bodyPartsList2)>0:
                bodyPartsList2[0].color(newColor2)
                #print("moving the neck")
                bodyPartsList2[0].goto(head2.xcor(),head2.ycor())

            
                


            time.sleep(delay)
    


wn.onkeypress(up,"w")
wn.onkeypress(down,"s")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.onkeypress(pause,"p")
wn.onkeypress(normal,"n")
wn.onkeypress(PVP,"v")
wn.onkeypress(up2,"Up")
wn.onkeypress(down2,"Down")
wn.onkeypress(left2,"Left")
wn.onkeypress(right2,"Right")
wn.listen() 






wn.mainloop()
