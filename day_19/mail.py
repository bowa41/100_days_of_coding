from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
screen.bgcolor("black")
user_bet = screen.textinput(title="Make your Bet.", prompt="Which Turtle will win the race?  Enter a color: ")
colors = ["red", "green", "orange", "yellow", "blue", "purple"]
all_turtles = []
y=-150

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    all_turtles.append(new_turtle)
    all_turtles[-1].color(colors[0])
    colors.pop(0)
    all_turtles[-1].penup()
    all_turtles[-1].goto(x=-230, y=y)
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've Lost! The {winning_color} is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
