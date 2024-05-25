import time
from turtle import Screen

import scoreboard
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

player_wins = False
game_is_on = True

while game_is_on:
    for n in range(0, 6):
        player_wins = player.check_win()
        time.sleep(0.1)
        screen.update()
        if n == 0:
            car.create_car()
        car.move_cars()
            # Detect collision with car
    for cars in car.cars_list:
        if player.distance(cars) < 20:
                scoreboard.game_over()
                game_is_on = False
    if player_wins:
        player.go_to_start()
        car.increase_speed()
        scoreboard.score_point()


screen.exitonclick()