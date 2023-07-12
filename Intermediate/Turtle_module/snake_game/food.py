from turtle import Turtle
import random



class Food(Turtle):
    """Creates a turtle by inheriting the turtle function's attributes with super function and passing it as an argument\n also initializes it in a random location using the refresh function"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid= 0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        """Randomizes and X and Y coordinates for the goto function to place the turtle"""
        random_x = random.randint(-265, +265)
        random_y = random.randint(-265, +265)
        self.goto(random_x, random_y)