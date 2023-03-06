from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager(Turtle):
  def __init__(self):
    super().__init__()
    self.car_list = []
    self.car_speed = STARTING_MOVE_DISTANCE


  def create_car(self):
    if random.randint(1, 6) == 1:
      self.car = Turtle()
      self.car.shape("square")
      self.car.turtlesize(stretch_len=2)
      self.car.color(random.choice(COLORS))
      self.car.penup()
      self.car.goto(self.get_car_position())
      self.car.seth(180)
      self.car_list.append(self.car)
    self.move()

  def move(self):
    for car in self.car_list:
      car.forward(self.car_speed)

  def new_level(self):
    self.reset_pos()    
    self.car_speed += MOVE_INCREMENT

  def reset_pos(self):
    for car in self.car_list:
      car.goto(self.get_car_position())

  def get_car_position(self):
    found_y_position = False
    new_x = 300
    
    while not found_y_position:
      new_y = random.randrange(-250, 250, 50)
      if len(self.car_list) > 0:
        for car in self.car_list:
          if car.ycor() != new_y:
            found_y_position = True
        return (new_x, new_y)
      else:
        return (new_x, new_y)
