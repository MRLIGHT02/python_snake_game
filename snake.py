from turtle import Turtle

STARTING_POSTIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT= 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color('red')
        
    
    
    def create_snake(self):
        
        for position in STARTING_POSTIONS:
            self.add_segment(position)
            
            # new_postion.shapes(4)
    def add_segment(self,position): 
            new_postion= Turtle("square")
            new_postion.color("white")
            new_postion.penup()
            new_postion.goto(position)                      
            self.segments.append(new_postion)
    def exten_snake(self):
        self.add_segment(self.segments[-1].position())
                
    def move_step(self):
        for new_segment in range(len(self.segments)-1,0,-1):
            new_x = self.segments[new_segment -1].xcor()
            new_y = self.segments[new_segment -1].ycor()
            self.segments[new_segment].goto(new_x,new_y)
        self.head.fd(MOVE_DISTANCE)   
            
           
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)            