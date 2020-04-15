import turtle
import random
import tkinter as tk
import time

cycles = input("How many cycles do you want? (choose a number greater than 0): ")
colour = input("Pick a colour: ")

win = turtle.Screen()
win.title("Random Art")

turtle.setx(0)
turtle.sety(0)

print("Generating art, please wait")

time.sleep(5)

while True:
    x = random.randrange(-1000, 750)
    y = random.randrange(-1000, 750)

    turtle.color(colour)
    turtle.speed(0)
    turtle.setx(x)
    turtle.sety(y)

    cycles = int(cycles)
    cycles -= 1

    if cycles <= 0:
        break

print("Art generated successfully, please check your tabs")

tk.mainloop()
