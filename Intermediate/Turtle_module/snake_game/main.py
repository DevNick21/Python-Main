from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


#using the screen class in turtle
screen = Screen()
#setting up the screen to the game screen size
screen.setup(width=600, height=600)
#setting the background color to black
screen.bgcolor("black")
#setting the title of the game screen
screen.title("My Snake Game")
#turning off the animation of the screen so it can render when we want it to
screen.tracer(0)





#calls the snake function thereby creating a new snake
scoreboard = Scoreboard()
snake = Snake()
food = Food()

#Listens for the key stroke of the arrow keys and performs the functions allocated to them
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")





game_is_on = True

while game_is_on:
    #updating the screen when needed
    screen.update()
    #suspends the execution by that given time
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    #Checks if the snake's head is less than 15 blocks of the food turtle to reset its position with the refresh method and also extend its..
    #tail withe the extend method and the increases the score with the increase score method
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    #Checks for the head coordinates to see if it is within the range of the screen walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_game()
        snake.reset_snake()


    #Detect collision with tail
    #Loops through tims(list of all the tims) and checks if the head distance is less than 10 blocks so it can turn off the game
    for tim in snake.tims[1:]:
        if snake.head.distance(tim) < 10:
            scoreboard.reset_game()
            snake.reset_snake()

































screen.exitonclick()