import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()
  car.create_car()
  car.move()

  # detect player move key
  screen.onkey(player.move, "Up")

  # player win level if reaches the top wall
  if player.check_if_finish():
    player.new_level()
    scoreboard.new_level()
    car.new_level()

  # detect player collition with cars
  for c in car.car_list:
    if c.distance(player) < 20:
      game_is_on = False
      scoreboard.game_over()