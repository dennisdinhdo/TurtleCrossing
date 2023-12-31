from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.setpos(x=-230,y=260)
        self.update()

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.level = 0
        self.setpos(x=0, y=0)
        self.write("GAME OVER", align="center", font=FONT)