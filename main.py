from turtle import Turtle, Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard


# TODO 1. Create the Screen
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=900, height=450)
my_screen.title("Ping Pong Game")
my_screen.tracer(0)

scoreboard = Scoreboard()

# TODO 2. Create and move the paddle

r_paddle = Paddle((420,0))
l_paddle = Paddle((-420, 0))


my_screen.listen()
my_screen.onkey(r_paddle.upper, "Up")
my_screen.onkey(r_paddle.lower, "Down")
my_screen.onkey(l_paddle.upper, "w")
my_screen.onkey(l_paddle.lower, "s")






# TODO 3. Create another paddle

# TODO 4. Create the ball and
#  make it move

ball = Ball()

# TODO 5. Detect collision with wall
#  and bounce

# TODO 6. detect collision with paddle

# TODO 7. Detect when paddle misses

# TODO 8. Keep score

bouncing = 0
ball_speed = 0.01  # Start speed: 0.05 seconds between moves

game_on = True
while game_on:

    my_screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 210 or ball.ycor() < -210:
        ball.bounce_y()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -400:
        ball.bounce_x()

    elif ball.distance(r_paddle) < 50 and ball.xcor() > 400:
        ball.bounce_x()
    if ball.xcor() > 420:
        ball.reset_ball()
        scoreboard.l_point()
        time.sleep(1)

    if ball.xcor() < -420:
        ball.reset_ball()
        scoreboard.r_point()
        time.sleep(1)


my_screen.exitonclick()