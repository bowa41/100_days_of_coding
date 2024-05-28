# import colorgram as c
# colors = c.extract('image.jpg', 30)
# color_list =[]
#
# for color in colors:
#
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     color_list.append((red,green,blue))
# print(color_list)
import turtle as t
import random
tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)
tim.hideturtle()
tim.speed('fastest')
tim.pensize(10)
tim.teleport(-500,-500)
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]


for i in range(-500,500,100):
    tim.teleport(-500, i)
    for _ in range(1,11):
        tim.dot(50,random.choice(color_list))
        tim.up()
        tim.forward(100)


screen = t.Screen()
screen.exitonclick()