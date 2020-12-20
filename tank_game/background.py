import turtle


#drawing the border of our game
def background_game():
    border_game = turtle.Turtle()
    border_game.color("white")
    border_game.penup()
    border_game.speed(0)
    border_game.setposition(-380, -380)
    border_game.pendown()
    border_game.pensize(3)
    for side in range(4):
        border_game.fd(760)
        border_game.lt(90)
    border_game.hideturtle()

background_game
