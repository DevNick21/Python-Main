import turtle as t
import random

tim = t
t.colormode(255)

#TODO Changing Turtle Shape and color
# tim.shape("turtle")
# tim.color("DarkCyan")

#TODO - Making it make a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#TODO - Making it make dotted lines
# for _ in range (15):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

#TODO - Making it draw all different sided shapes
# sides = [3, 4, 5, 6, 7, 8, 9, 10]
# colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

# for side in sides:
#     tim.pencolor(random.choice(colors))
#     for _ in range(side):
#         tim.forward(100)
#         tim.right(360 / side)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

#TODO - Making it do a random walk with random colors

# direction = [0, 90, 180, 270]

# times = 200
# tim.speed("fastest")
# tim.pensize(5)
# def move ():
#     tim.forward(5)
#     tim.seth(random.choice(direction))
#     tim.pencolor(random_color())
#     tim.forward(5)

# for _ in range(times):
#     move()

#TODO - Making it do draw a spirograph
tim.speed("fastest")
def draw(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        # tim.left(_)


draw(5)











screen = t.Screen()
screen.exitonclick()
