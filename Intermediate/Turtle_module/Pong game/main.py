from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
#setting up the screen to the game screen size
screen.setup(width=800, height=600)
#setting the background color to black
screen.bgcolor("black")
#setting the title of the game screen
screen.title("Pong")
#turning off the animation of the screen so it can render when we want it to
screen.tracer(0)









score = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()




screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")





game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.deflect_y()
    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50  and ball.xcor() < -320:
        ball.deflect_x()
    #Detect R paddle miss
    if ball.xcor() > 380:
        ball.ball_out()
        score.point("left")
    #Detect L paddle miss
    if ball.xcor() < -380:
        ball.ball_out()
        score.point("right")























screen.exitonclick()
