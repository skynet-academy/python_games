import turtle


class Character:
    def __init__(self):
        self.speed_turtle = 10
        self.player = turtle.Turtle()
        #self.#player.color("blue")
        self.player.shape('tank.gif')
        #self.#player.shape()
        self.player.turtlesize(5)
        self.player.penup()
        self.player.speed(0)
        self.player.setposition(0,-250)
        self.player.setheading(90)

    def move_left(self):
        x = self.player.xcor()
        x -= self.speed_turtle
        if(x < -365):
            x = -365
        self.player.setx(x)

    def move_right(self):
        x = self.player.xcor()
        x += self.speed_turtle
        if(x > 365):
            x = 365
        self.player.setx(x)

    def move_forward(self):
        y = self.player.ycor()
        y += self.speed_turtle
        if(y > 365):
            y = 365
        self.player.sety(y)

    def move_backguard(self):
        y = self.player.ycor()
        y -= self.speed_turtle
        if(y < -365):
            y = -365
        self.player.sety(y)



