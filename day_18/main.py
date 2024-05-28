import random
import turtle as t
import colorgram

tim = t.Turtle()
screen = t.Screen()
tim.shape("turtle")
tim.color("red", "SteelBlue")
screen.colormode(255)


tim.speed('fastest')
tim.pensize(2)
def change_color():
    R = random.randint(0, 255)
    B = random.randint(0, 255)
    G = random.randint(0, 255)
    color = (R, G, B)
    return color

for i in range(0,361, 4):
    tim.circle(100)
    heading = int(i)
    tim.setheading(heading)
    tim.pencolor(change_color())




screen = t.Screen()
screen.exitonclick()