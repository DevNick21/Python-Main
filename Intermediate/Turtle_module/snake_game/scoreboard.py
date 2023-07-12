from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 16, "normal")

class Scoreboard(Turtle):
    """Inherits the turtle class and creates a turtle which would be a text"""
    def __init__(self):
        """Initializes the written turtle and calls the update_scoreboard function to display the initialized score"""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        """updates the score"""
        self.write(arg=f"Score: {self.score} ", align= ALIGNMENT, font= FONT)

    def game_over(self):
        """displays GAME OVER and its rendered at the home position"""
        self.goto(0, 0)
        self.write(arg="GAME OVER", align= ALIGNMENT, font= FONT)



    def increase_score(self):
        """Increases the score and clears the turtle and replaces it with a new scoreboard with a new score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()


