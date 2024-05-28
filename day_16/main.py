# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepSkyBlue", "coral4")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokkemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electrical", "Water", "Fire"])
table.align = "l"
print(table)