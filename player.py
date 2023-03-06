from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.color("black")
    self.penup()
    self.goto(0, -280)
    self.seth(90)

  def move(self):
    self.forward(MOVE_DISTANCE)
    self.check_if_finish()


  def check_if_finish(self):
    if self.ycor() >= FINISH_LINE_Y: 
      return True
    else:
      return False
    
  def new_level(self):
    self.goto(0, -280)
