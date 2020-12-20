import turtle


class Enemy:
    def __init__(self):
        self.speed_turtle = 9
        self.enemy = turtle.Turtle()
        self.enemy.color("blue")
        self.enemy.shape('circle')
        self.enemy.turtlesize(2)
        self.enemy.penup()
        self.enemy.speed(0)
        self.enemy.setposition(200,200)
        self.enemy.setheading(270)

    #def move_left(self):
    #    x = self.enemy.xcor()
    #    x -= self.speed_turtle
    #    if(x < -365):
    #        x = -365
    #    self.enemy.setx(x)

    #def move_right(self):
    #    x = self.enemy.xcor()
    #    x += self.speed_turtle
    #    if(x > 365):
    #        x = 365
    #    self.enemy.setx(x)

    #def move_forward(self):
    #    y = self.enemy.ycor()
    #    y += self.speed_turtle
    #    if(y > 365):
    #        y = 365
    #    self.enemy.sety(y)

    #def move_backguard(self):
    #    y = self.enemy.ycor()
    #    y -= self.speed_turtle
    #    if(y < -365):
    #        y = -365
    #    self.enemy.sety(y)


