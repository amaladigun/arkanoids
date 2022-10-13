import turtle
import time

# Define Global Variables
score = 0
delay = 0.01

#Setting up the screen, title, background color, width etc.
# must return the window created
def setUpScreen():
    # Set up the screen
    wn = turtle.Screen()
    wn.title('Arkanoid - Save the Ball!')
    # Set background color
    wn.bgcolor('light green')
    # Set height and width
    wn.setup(width = 800, height = 600)
    # Turns off the screen updates
    wn.tracer(0)
    return wn

# Create and return the paddle
def createPaddle():
    paddle = turtle.Turtle()
    # Set speed, shape, color and penup
    paddle.color('teal')
    paddle.shape('square')
    paddle.speed(0)
    paddle.penup()
    # move paddle to the bottom of the screen
    paddle.goto(0,-250)
    paddle.shapesize(0.5, 6)
    return paddle

# Create and return the ball
def createBall():
    ball = turtle.Turtle()
    # Set speed, shape, color and penup
    ball.color('teal')
    ball.shape('circle')
    ball.speed(0)
    ball.penup()
    # setting delta for the ball movement 
    ball.dx = 3 
    ball.dy = 3
    return ball

# Write score and highscore on the screen
def trackScoreOnScreen():
    pen = turtle.Turtle()
    # Set color, speed
    pen.color('teal')
    pen.speed(0)
    # penup and hide turtle
    pen.penup()
    pen.hideturtle()
    # Move the score to top of screen
    pen.goto(0,260)
    pen.write("Score: 0", align='center', font=('Times New Roman', 24, 'bold'))
    return pen

# Function to be called by pressing left key 
# It will help to move paddle in left direction to save ball from falling down
def paddle_left():
    # remove print statement after implementing this function
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)

# Function to be called by pressing right key 
# It will help to move paddle in right direction to save ball from falling down
def paddle_right():
    # remove print statement after implementing this function
    x = paddle.xcor()
    x += 20
    x = paddle.setx(x)


# Bind Left and Right keys with their function
def bindKeyboardKeys(wn):
    # remove print statement after implementing this function
    wn.listen()
    wn.onkeypress(paddle_left, 'Left')
    wn.onkeypress(paddle_right, 'Right')

# Function to call to move the ball automatically
# should be called from the main loop. 
def moveBall():
    # Moving Ball
    # remove print statement after implementing this function
    x = ball.xcor()
    x = x + ball.dx
    ball.setx(x)
    y = ball.ycor()
    y = y + ball.dy
    ball.sety(y)
    
# detect collision of ball with the borders and handle the bounce of the ball
def detectHandleBallCollisionWithBorders(ball, trackScore):
    global score
    global delay
    # Border checking
    # check left and right border
    if ball.xcor() > 390 or ball.xcor() < -390:
       ball.dx = ball.dx * -1
       # remove print statement after implementing this function
        

    # check top border
    if ball.ycor() > 290:
        # remove print statement after implementing this function
        ball.dy = ball.dy * -1   
        print('move ball in y axis backward direction')

    # check bottom border , if ball go below this it will fall
    if ball.ycor() < -290:
        ball.goto(0,0)
        # set the ball at origin
        ball.dy *= -1
        # Reset the score
        score = 0
        # Reset the delay
        delay = 0.02
        # Clear trackscore and start from 0
        trackScore.clear()
        trackScore.write("Score: {}".format(score), align='center', font=('Courier', 24, 'bold'))
    print("detectHandleBallCollisionWithBorders function called")

# detect and handle collision of the ball with the paddle
# if ball will touch the paddle, increment score by , push ball upwards, reduce the delay
def detectHandleBallCollisionWithPaddle(ball, trackScore, paddle):
    global score
    global delay
    if (ball.ycor() < -245 and ball.ycor() > -255) and (ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50) :
        # push ball upwards
        ball.dy = ball.dy * -1
        # increment the score
        score = score +1
        # Shorten the delay, to move ball faster
        delay -= 0.001
        trackScore.clear()
        trackScore.write("Score: {}".format(score), align='center', font=('Courier', 24, 'bold'))
        # update score on the screen
    print("detectHandleBallCollisionWithPaddle function called")


####################################
#                                  #
#   Start of the main function     #
#                                  #
####################################

#Call Functions in main program
wn = setUpScreen()
ball = createBall()
paddle = createPaddle()
trackScore = trackScoreOnScreen()
bindKeyboardKeys(wn)

# Start of main game loop
while True:
    wn.update()
    
    # check and handle ball collision with the borders
    detectHandleBallCollisionWithBorders(ball, trackScore)
    
    # check and handle ball collision with the paddle
    detectHandleBallCollisionWithPaddle(ball, trackScore, paddle)
    
    # keep the ball moving
    moveBall()
    
    time.sleep(delay)

wn.mainloop()