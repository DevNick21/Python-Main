from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    """Class to initialize the snake"""
    def __init__(self):
        """Calls the create_snake function and intializes the list of turtles(tims) to an empty list to be appended\nIt also initializes the head of the snake after calling the create_snake function, so that the head of the snake can be controlled independently"""
        self.tims = []
        self.create_snake()
        self.head = self.tims[0]

    def create_snake(self):
        """A method the Loops through the constant STARTING_POSITIONS to create a starting position for a new snake and then calls the add_tim function"""
        for position in STARTING_POSITIONS:
            self.add_tim(position)


    def add_tim(self, position):
        """Creates a new turtle with the turtle class and makes it a square to fit the description required for the snake game and the appends it to the list so the can be controlled evenly with the positions"""
        new_tim = Turtle("square")
        new_tim.color("white")
        new_tim.penup()
        new_tim.goto(position)
        self.tims.append(new_tim)

    def reset_snake(self):
        for tim in self.tims:
            tim.goto(1000, 1000)
        self.tims.clear()
        self.create_snake()
        self.head = self.tims[0]



    def extend(self):
        """adds another square turtle object which makes for the extension of the tail by calling the add_tim method and passing the last tim with -1 then getting its position so that the new tim would be rendered there"""
        self.add_tim(self.tims[-1].position())

    def move(self):
        """A method that loops through the length of the tims - 1 backwards, starting from the last and making each last tim move to the next's position before it while moving the first tim by the constant"""
        for tim_num in range(len(self.tims) - 1, 0, -1):
            new_x = self.tims[tim_num -1].xcor()
            new_y = self.tims[tim_num -1].ycor()
            self.tims[tim_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Makes snake go upwards"""
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        """Makes snake go downwards"""
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        """Makes snake go right"""
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        """Makes snake go left"""
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)










