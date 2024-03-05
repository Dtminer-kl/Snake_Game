from turtle import Turtle

FONT = ('arial', 13, 'bold')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.print_score()


    def print_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align='center', font=FONT)


    def increase(self):
        self.score += 1
        self.print_score()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
                self.high_score = self.score
        self.score = 0
        self.print_score()





