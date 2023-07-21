from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
user_level = input("choose level hard= h ,medium = m ,easy = e \n").lower()
screen  = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
    
is_game_on = True

while is_game_on:
    screen.update()
    if  user_level == 'h':
        time.sleep(0.1)
    elif user_level == 'm':
        time.sleep(0.2)
    else:
        time.sleep(0.5)
    time.sleep(0.1)
                             
    snake.move_step()
    
    
    # detect the distance 
    if snake.head.distance(food)<15:
        food.refresh_food() 
        snake.exten_snake()
        score.increase_score()
   
    
            
    
    # dectect colision of wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 280 or snake.head.ycor() < -295 :
        is_game_on = False 
        score.game_over() 
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<5:
            is_game_on = False
            score.game_over()
                   

    
screen.exitonclick()


