#pvc version
import turtle as t 
import random as rand

# variables
courtHeight=600
courtWidth=1000
ballSpeed=12
ballSize=15
paddleWidth=39
scoreRed=0
scoreBlue=0
fontSettings=("Arial" ,44,"normal")


#functions

def drawField():
    #draw out the border
    border = t.Turtle(visible=False)
    border.speed(0)
    border.color("white")
    border.pensize(3)
    border.penup()

    #draw the top border
    border.goto(courtWidth/-2,courtHeight/2)
    for i in range(2):
        border.pendown()
        border.forward(courtWidth)
        border.penup()
        border.right(90)
        border.forward(courtHeight)
        border.right(90)
    #draw the halfcourt line
    border.setx(0)
    border.right(90)
    for i in range(courtHeight//50):
        border.pendown()
        border.forward(26)
        border.penup()
        border.forward(26)
        
def collideWithPaddle(paddle,b):
    global ballSpeed
    if paddle.distance(b)<paddleWidth:
        b.setheading(180-b.heading())
        if b.xcor()>0:
            b.setx(b.xcor()-5)
        else:
            b.setx(b.xcor()+5)
        ballSpeed+=5
        b.forward(ballSpeed)


#move function
def move():
    global scoreBlue, scoreRed, ballSpeed
    ball.forward(ballSpeed)
    x,y=ball.position()
    redPlayer.sety(ball.ycor())
    computer()

    #things we need to check for when the ball moves
    #   1: did it hit a paddle?
    #   2: did it hit the top or bottom wall?
    #   3: did it go off the edge?
    #       a: if it went off the left edge blue gets a point
    #       b:if it went off the right edge red gets a point






    if x>courtWidth/2 :      #right wall        red scores a point
        scoreRed+=1
        sRed.clear()
        sRed.write(scoreRed,font=fontSettings)
        resetBall()
        ballSpeed=12
    elif x<-courtWidth/2:       #left wall      Blue scores a point
        scoreBlue+=1
        sBlue.clear()
        sBlue.write(scoreBlue,font=fontSettings)
        resetBall()
        ballSpeed=12
    elif y>(courtHeight/2-ballSize) or y<(-courtHeight/2+ballSize) :       #top and bottom wall
        ball.setheading(-ball.heading())
    else:                       #checks to see if it hit paddle
        collideWithPaddle(redPlayer,ball)
        collideWithPaddle(bluePlayer,ball)



    wn.ontimer(move,20) #example of recursion

def resetBall():
    ball.goto(0,0)
    side=rand.randint(0,1)
    if side==1:
        ball.setheading(rand.randint(-45,45))
    else:
        ball.setheading(rand.randint(135,225))

def computer():
    if ball.xcor()<=(-460):
        comp=rand.randint(0,100)
        print(comp)
        if comp<=50:
            redPlayer.sety(ball.ycor())
        else:
            redPlayer.sety(redPlayer.ycor()-100)


def upRed():
    y=redPlayer.ycor()
    if  y<(courtHeight/2-paddleWidth):
        redPlayer.sety(y+20)

def downRed():
    y=redPlayer.ycor()
    if y>(courtHeight/-2+paddleWidth) :
        redPlayer.sety(y-20)

def upBlue():
    y=bluePlayer.ycor()
    if y<(courtHeight/2-paddleWidth):
        bluePlayer.sety(y+20)

def downBlue():
    y=bluePlayer.ycor()
    if y>(courtHeight/-2+paddleWidth) :
        bluePlayer.sety(y-20)



#turtles


#redpaddle = speed="0",color,position set to the edge of the screen
redPlayer=t.Turtle()
redPlayer.speed(0)
redPlayer.penup()
redPlayer.color("red")
redPlayer.shape("square")
redPlayer.shapesize(3,2)
redPlayer.setx(courtWidth/-2)

#red score turtle
sRed=t.Turtle(visible=False)
sRed.speed(0)
sRed.color("white")
sRed.penup()
sRed.setposition(-courtWidth/4,courtHeight/4)
sRed.write(scoreRed,font=fontSettings)

#bluepaddle
bluePlayer=t.Turtle()
bluePlayer.speed(0)
bluePlayer.penup()
bluePlayer.color("blue")
bluePlayer.shape("square")
bluePlayer.shapesize(3,2)
bluePlayer.setx(courtWidth/2)

#blue score turtle
sBlue=t.Turtle(visible=False)
sBlue.speed(0)
sBlue.color("white")
sBlue.penup()
sBlue.setposition(courtWidth/4,courtHeight/4)
sBlue.write(scoreBlue,font=fontSettings)


#ball
ball=t.Turtle("circle")
ball.color("white")
ball.penup()
ball.speed(0)
ball.setheading(rand.randint(-45,45))


#to make the computer win a couple times do what we did to pick 1 or 2 randomly to see which way the ball went. make it to choose 1 or 2 to see if the computer paddle will get to the ball or if the player will score on it


wn = t.Screen()
wn.bgcolor("black")
wn.setup(width=1200,height=800 )

wn.onkeypress(resetBall,"r")
#wn.onkeypress(upRed,"w")
#wn.onkeypress(downRed,"s")
wn.onkeypress(upBlue,"i")
wn.onkeypress(downBlue,"k")
wn.listen()

drawField()
move()

wn.mainloop()