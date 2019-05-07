# ex30 - Pong, by Nicholas Small
#
# following https://www.youtube.com/playlist?list=PLlEgNdBJEO-kXk2PyBxhSmo84hsO3HAz2
#
# bounce.wav is from the website in the description of the videos
# score.wav was made by myself in Audacity

import turtle
import winsound  # only works on Windows

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.pu()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.pu()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.pu()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.ht()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 18))

# move paddle function
def move_paddle(paddle, dir):
    y = paddle.ycor()
    if dir == "up":
        y += 20
    elif dir == "down":
        y -= 20
    paddle.sety(y)

# no-parameter functions
def paddle_a_up():
    move_paddle(paddle_a, "up")
def paddle_a_down():
    move_paddle(paddle_a, "down")
def paddle_b_up():
    move_paddle(paddle_b, "up")
def paddle_b_down():
    move_paddle(paddle_b, "down")

# keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

top_border = 290
bottom_border = -290
right_border = 390
left_border = -390

# main game loop
while True:
    win.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > top_border:
        ball.sety(top_border)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    elif ball.ycor() < bottom_border:
        ball.sety(bottom_border)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > right_border:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 18))
    elif ball.xcor() < left_border:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 18))
    
    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)