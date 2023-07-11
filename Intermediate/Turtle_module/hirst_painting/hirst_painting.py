import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# import colorgram

# colors = colorgram.extract("Intermediate/Turtle_module?hirst_painting/image.jpg", 50)

# color_list = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color =(r, g, b)
#     color_list.append(new_color)

# print(color_list)


final_colors_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]

vertical = -300
horizontal = -300
while vertical < 151:
    tim.setpos(horizontal, vertical)
    tim.dot(20, random.choice(final_colors_list))
    while horizontal < 151:
        tim.setpos(horizontal, vertical)
        tim.dot(20, random.choice(final_colors_list))
        horizontal += 50
    horizontal = -300

    vertical += 50


























screen = t.Screen()
screen.exitonclick()