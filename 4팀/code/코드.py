import turtle as t
import random
import time

def right():
    if player.xcor() <160:
        player.forward(30)
def left():
    if player.xcor() >-160:
        player.backward(30)

t.bgcolor("lightpink")
t.setup(450, 600)

#플레이어 객체
player= t.Turtle()
player.shape("square")
player.shapesize(1,5)
player.up()
player.speed(0)
player.goto(0,-250)

#ball
ball =t.Turtle()
ball.shape("circle")
ball.shapesize(1.3)
ball.up()
ball.speed(0)
ball.color("white")


t.listen()
t.onkeypress(right, "Right")
t.onkeypress(left, "Left")


ball_xspeed =3
ball_yspeed =3

game_on=True
life=3

#점수표시
t.up()
t.ht()
t.goto(0,250)
t.write(f"life : {life}", False, "center", ("",20))

while game_on:
    new_x=ball.xcor() +ball_xspeed
    new_y=ball.ycor() +ball_yspeed
    ball.goto(new_x,new_y)

    if ball.xcor() >200 or ball.xcor() <-200:
        ball_xspeed*=-1

    if ball.ycor()>300:
        ball_yspeed*=-1

    if ball.ycor() <-300:
        life -= 1
        t.clear()
        t.write(f"life : {life}", False, "center", ("",20))
        time.sleep(0.5)
        ball.goto(0,100)
        ball_xspeed*=-1
        ball_yspeed*=-1

    if life==0:
        game_on=False
        t.goto(0,0)
        t.write("Game Over", False, "center", ("",20))

    if player.distance(ball) <50 and -250 < ball.ycor() <-235:
        ball_yspeed*=-1