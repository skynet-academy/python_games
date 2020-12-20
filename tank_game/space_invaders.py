import turtle
import os
import background 

from character import Character
from enemy import Enemy



#our window
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invader - Python")
window.register_shape('tank.gif')
#window.bgpic('tank.gif')   // to add as a background
background.background_game()
character = Character()
enemy = Enemy()

#Creating keyboard bindings 

turtle.listen()
turtle.onkey(character.move_left, "Left")
turtle.onkey(character.move_right, "Right")
turtle.onkey(character.move_forward, "Up")
turtle.onkey(character.move_backguard, "Down")


#while(True):
#    # moving enemy
#    x = enemy.xcor()
#    x += enemy_speed
#    enemy.setx(x)
#    
#    # 
#    if( enemy.xcor() > 365):
#        enemy_speed *=-1
#    if( enemy.xcor() < -365):
#        enemy_speed *=-1






turtle.mainloop()

