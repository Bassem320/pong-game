from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 260)
        self._update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self._update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self._update_scoreboard()


    def _update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))
