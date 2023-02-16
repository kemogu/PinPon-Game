import turtle

##### Ping Pong game made by kemoguBH #####

# Game Screen
window = turtle.Screen()
window.title("PinPon")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle Left
paddleLeft = turtle.Turtle()
paddleLeft.speed(0)
paddleLeft.shape("square")
paddleLeft.color("white")
paddleLeft.shapesize(stretch_wid=5, stretch_len=1)
paddleLeft.penup()
paddleLeft.goto(-350, 0)

# Paddle Right
paddleRight = turtle.Turtle()
paddleRight.speed(0)
paddleRight.shape("square")
paddleRight.color("white")
paddleRight.shapesize(stretch_wid=5, stretch_len=1)
paddleRight.penup()
paddleRight.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Score
scoreLeft = 0
scoreRight = 0


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A = 0 Player B = 0 ", align="center", font = ("New Times Roman", 20 ," normal"))


# Movement Functions of Paddle Left
def paddleLeft_up():
    y = paddleLeft.ycor()
    y += 30
    paddleLeft.sety(y)

def paddleLeft_down():
    y = paddleLeft.ycor()
    y -= 30
    paddleLeft.sety(y)

# Movement Functions of Paddle Right
def paddleRight_up():
    y = paddleRight.ycor()
    y += 30
    paddleRight.sety(y)

def paddleRight_down():
    y = paddleRight.ycor()
    y -= 30
    paddleRight.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(paddleLeft_up, "w")
window.onkeypress(paddleLeft_down, "s")
window.onkeypress(paddleRight_up, "Up")
window.onkeypress(paddleRight_down, "Down")


# Game Loop
while True:

    window.update()
    window.listen()
    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Control
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *=-1
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390 :
        ball.goto(0, 0)
        ball.dx *= -1
        scoreLeft += 1
        pen.clear()
        pen.write("Player A = {} Player B = {} ".format(scoreLeft, scoreRight), align="center", font=("New Times Roman", 20, " normal"))
    if ball.xcor() < -390 :
        ball.goto(0, 0)
        ball.dx *= -1
        scoreRight += 1
        pen.clear()
        pen.write("Player A = {} Player B = {} ".format(scoreLeft, scoreRight), align="center", font=("New Times Roman", 20, " normal"))

    # Paddle and ball contact
    if ((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleRight.ycor() + 50 and ball.ycor() > paddleRight.ycor() - 50)) :
        ball.setx(340)
        ball.dx *= -1
    if ((ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleLeft.ycor() + 50 and ball.ycor() > paddleLeft.ycor() - 50)) :
        ball.setx(-340)
        ball.dx *= -1



