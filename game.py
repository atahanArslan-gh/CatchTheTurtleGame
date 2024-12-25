import turtle
import random

#screen
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ('Arial', 30, 'normal')
game_over = False
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [-20, -10, 0, 10, 20]
turtle_list = []
grid_size = 15
score = 0

#score turtle
score_turtle = turtle.Turtle()
def set_score_turtle():
    score_turtle.penup()
    score_turtle.hideturtle()
    score_turtle.color('dark blue')

    top_height = screen.window_height() / 2
    y_score = top_height * 0.9
    score_turtle.setpos(x=0, y=y_score)
    score_turtle.write(arg='Score: 0', move=False, align='center', font=FONT)

#turtles
def make_turtle(x, y):
    t = turtle.Turtle()
    def handle_click(x, y):
        global score
        score +=1
        score_turtle.clear()
        score_turtle.write(arg=f'Score: {score}', move=False, align='center', font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape('turtle')
    t.shapesize(2.5, 2.5)
    t.color('dark green')
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)

def set_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(fun=show_turtles_randomly, t=600)

#countdown turtle
countdown_turtle = turtle.Turtle()
def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color('dark blue')
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setpos(x=0, y=y)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f'Time: {time}', move=False, align='center', font=FONT)
        screen.ontimer(fun=lambda: countdown(time - 1), t=1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg='GAME OVER!!!', move=False, align='center', font=FONT)


turtle.tracer(0)
countdown(60)
set_score_turtle()
set_turtles()
hide_turtles()
show_turtles_randomly()
turtle.tracer(1)

turtle.mainloop()