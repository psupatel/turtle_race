import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "green", "blue", "purple", "pink", "orange"]
racers = []
user_choice = screen.textinput("Pick a turtle", "What color do you think will win?")
race_is_on = False

x_pos = -230
y_pos = 150

# create new turtles and add them to the 'racers' list
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.setposition(x_pos, y_pos)
    racers.append(new_turtle)
    y_pos -=60

race_is_on = True

while race_is_on:
    for racer in racers:
        if racer.xcor() > 220:
            race_is_on = False
            winning_turtle = racer.pencolor()
            if winning_turtle == user_choice:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")

        racer.forward(random.randint(0, 10))

screen.exitonclick()

