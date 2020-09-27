'''Pong game'''

import turtle#.....................................Module that gives objects diffrent abilities 

wn = turtle.Screen()#..............................Title screen creation
wn.title("Pong by @PittsPreneur")#.................Creates the title screen
wn.bgcolor("black")#...............................Sets the coor for the background
wn.setup(width=800,height=600)#....................Dimensions of the screen
wn.tracer(0)#......................................???????

score_a = 0
score_b = 0

paddle_a = turtle.Turtle()#........................Assigning tutle to paddle_a (module.Class)
paddle_a.speed()#..................................
paddle_a.shape("square")#..........................
paddle_a.color("green")#...........................
paddle_a.shapesize(stretch_wid=5, stretch_len=1)#..
paddle_a.penup()#..................................
paddle_a.goto(-350, 0)#............................


paddle_b = turtle.Turtle()#........................Assigning tutle to paddle_b (module.Class)
paddle_b.speed()#..................................
paddle_b.shape("square")#..........................
paddle_b.color("green")#...........................
paddle_b.shapesize(stretch_wid=5, stretch_len=1)#..
paddle_b.penup()#..................................
paddle_b.goto(350, 0)#.............................

ball = turtle.Turtle()#............................Begining of Ball Oject
ball.speed()#......................................
ball.shape("square")#..............................
ball.color("green")#...............................
ball.penup()#......................................
ball.goto(0, 0)#...................................
ball.dx = 2#.......................................
ball.dy = 2#.......................................


pen = turtle.Turtle()#.............................Assigning turtle to pen (module.Class)
pen.speed(0)#......................................Scoreboard does not move, thus zero speed
pen.color("green")#................................Matches other element's colors
pen.penup()#.......................................Eliminates lines in the scoreboard
pen.hideturtle()#..................................Doesnt show the entire object, only the text
pen.goto(0,260)#...................................Declares the scoreboard position
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))#......





def paddle_a_up():
    y = paddle_a.ycor()#...........................Returns the y coordinates to variable "y"
    y += 20#.......................................Adds 20 pixels to the y coordinates d
    paddle_a.sety(y)#..............................

def paddle_a_down():
    y = paddle_a.ycor()#...........................Returns the y coordinates to variable "y"
    y -= 20#.......................................Adds 20 pixels to the y coordinates d
    paddle_a.sety(y)#..............................

def paddle_b_up():
    y = paddle_b.ycor()#...........................Returns the y coordinates to variable "y"
    y += 20#.......................................Adds 20 pixels to the y coordinates d
    paddle_b.sety(y)#..............................

def paddle_b_down():
    y = paddle_b.ycor()#...........................Returns the y coordinates to variable "y"
    y -= 20#.......................................Adds 20 pixels to the y coordinates d
    paddle_b.sety(y)#..............................


wn.listen()#.......................................
wn.onkeypress(paddle_a_up, "a")#...................
wn.onkeypress(paddle_a_down, "z")#.................
wn.onkeypress(paddle_b_up, "Up")#..................
wn.onkeypress(paddle_b_down, "Down")#..............


while True:#.......................................Initiates main game loop
    wn.update()#...................................

#...Ball Movement..................................
    ball.setx(ball.xcor() + ball.dx)#..............
    ball.sety(ball.ycor() + ball.dy)#..............

#...Ball Boundaries................................
    if ball.ycor() > 290:#.........................
        ball.sety(290)#............................
        ball.dy *= -1#.............................
        
    if ball.ycor() < -290:#........................
        ball.sety(-290)#...........................
        ball.dy *= -1#.............................

    if ball.xcor() > 390:#.........................
        ball.goto(0, 0)#...........................
        ball.dx *= -1#.............................
        score_a += 1#..............................Adds a score to Player A
        pen.clear()#...............................Clears the previous score number
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:#........................
        ball.goto(0, 0)#...........................
        ball.dx *= -1#.............................
        score_b += 1#..............................Adds a score to Player B
        pen.clear()#...............................Clears the previous score number
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #Paddle/Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):#...Sets Paddle B Paddle As an Object
        ball.setx(340)#............................Sets ball's collision
        ball.dx *= -1#.............................Reverses the direction and the ball's speed

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):#...Sets Paddle B Paddle As an Object
        ball.setx(-340)#............................Sets ball's collision
        ball.dx *= -1#.............................Reverses the direction and the ball's speed
        
    























        
    
    

















    
