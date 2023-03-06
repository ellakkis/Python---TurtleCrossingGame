from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.color("black")
    self.penup()
    self.hideturtle()
    self.level = 1
    self.update_scoreboard()
   

  def new_level(self):
    self.level += 1
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.goto(-200, 260)
    self.write(f"Level= {self.level}", move=False, align="left", font=FONT)

  def game_over(self):
    game_over_text = Turtle()
    self.goto(0, 0)
    self.write(f"GAME OVER!", move=False, align="left", font=FONT)
