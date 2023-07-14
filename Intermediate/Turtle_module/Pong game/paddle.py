from turtle import Turtle
HEIGHT_OF_PADDLE = 5
WIDTH_OF_PADDLE = 1
STARTING_POSITIONS = [(-350, 0),(350, 0)]



class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = HEIGHT_OF_PADDLE, stretch_len = WIDTH_OF_PADDLE)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)