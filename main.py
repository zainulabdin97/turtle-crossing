import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.listen()
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move_up, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car

    for car in car_manager.all_cars:

        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect when player reached the other side

    if player.is_at_finish_line():
        scoreboard.level += 1
        scoreboard.increment_level()
        player.go_to_start()
        car_manager.increase_car_speed()





screen.exitonclick()
