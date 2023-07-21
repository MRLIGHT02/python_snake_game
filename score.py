from turtle import Turtle

FONT = ("Courier",14,"normal")
GAME_FONT = ("Courier",24,"normal")
ALINMENT = "center"

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f"Score : {self.score}",align=ALINMENT,font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALINMENT,font=GAME_FONT)     
    def increase_score(self):
        self.score+=1        
        self.clear()
        self.update_scoreboard()                
        