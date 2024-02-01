import turtle
from random import randint
import keyboard 


while True:
    size = randint(0,100)
    turtle.color("red")

    if keyboard.is_pressed("r"):
        break
    else:
        turtle.color("green")
        turtle.circle(size)




