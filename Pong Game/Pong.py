#Simple pong game python 3
# First import turtle module it is good with graphics 
# #and it let's you build some basisc games, 
# #it is simpler than pygame because it is built in you don't have to install it
import turtle

window = turtle.Screen()

#Now we call a variable and call it window and do some customizations to it
window.title("Pong Game Kuaba")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#Main game loop
#This tracer thingy actually let's us update our game manually which makes it go faster

#So in this game we basically have 3 objects on the screen that we will add paddle 1 paddle 2 and a ball
#Each of these objects need a name
# We will turn names into turtle objects

#Paddle 1
pad1 = turtle.Turtle()
pad1.speed(0)
#This speed is not related to the speed of the pad (animation)
# #actually is an optimization measure for the turtle module animation in program to run at highest capacity
pad1.shape("square")
pad1.color("white")
pad1.penup()
# we're gonna change the size of the pad1 with this definition into an image we like
pad1.shapesize(stretch_wid=5, stretch_len=1)
#Did it, it looks like a cool rectangle now
pad1.goto(-350, 0)

#Paddle B
pad2 = turtle.Turtle()
pad2.speed(0)
pad2.shape("square")
pad2.color("white")
pad2.penup()
pad2.shapesize(stretch_wid=5, stretch_len=1)
pad2.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

#Function that wwill allow us to do stuff with our objects
#Function to: move each movement is a function i guess 4, going up and down on 2 paddles

#Function 1 pad1 up by pressing w
def pad1_up():
    y = pad1.ycor()
    y += 20
    pad1.sety(y)
#Function 2 pad1 down by pressing s
def pad1_down():
    y = pad1.ycor()
    y -= 20
    pad1.sety(y)

#Function 3 pad2 up by pressing up key
def pad2_up():
    y = pad2.ycor()
    y += 20
    pad2.sety(y)
#Function 4 pad2 down by pressing down key
def pad2_down():
    y = pad2.ycor()
    y -= 20
    pad2.sety(y)

#Keyboard biding
window.listen()
window.onkeypress(pad1_up, "w")
window.onkeypress(pad1_down, "s")
window.onkeypress(pad2_up, "Up")
window.onkeypress(pad2_down, "Down")


#Main Game Loop
while True:
    window.update()
    #Move the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
    
